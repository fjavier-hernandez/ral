#!/usr/bin/env python3
"""
md_to_pdf_converter.py
======================
Convierte Markdown → PDF usando Pandoc + Typst.

Características:
- Descarga diagramas Mermaid como PNG locales (mermaid.ink) y los embebe.
- Genera portada simple (título, subtítulo, autor, fecha) a partir del
  encabezado del propio documento (`#`, `**Módulo:**`, `**Temas:**`, `**Curso:**`).
- Activa TOC sólo si el documento es razonablemente largo (≥ 8 encabezados).
- Configura márgenes A4 y resaltado de sintaxis en bloques de código.
- Mantiene UTF-8 / acentos.
- No modifica los Markdown originales: trabaja sobre una copia en /tmp.

Uso:
    python3 Extra/md_to_pdf_converter.py        # convierte la lista por defecto
    python3 Extra/md_to_pdf_converter.py f1.md  # convierte ficheros pasados como args
"""
from __future__ import annotations

import base64
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
EXTRA = REPO_ROOT / "Extra"

DEFAULT_TARGETS = [
    "Examen_Enrutamiento_Unidad7_Modelo_A_Recuperacion.md",
    "Examen_Enrutamiento_Unidad7_Modelo_A_Recuperacion_Soluciones.md",
    "Examen_Tema_8_9_Modelo_B.md",
    "Examen_Tema_8_9_Modelo_B_Soluciones.md",
]


def b64url(s: str) -> str:
    return base64.urlsafe_b64encode(s.encode("utf-8")).rstrip(b"=").decode("ascii")


def fetch_mermaid_png(code: str, out: Path) -> bool:
    """Descarga el diagrama Mermaid renderizado como PNG."""
    url = f"https://mermaid.ink/img/{b64url(code)}?type=png&bgColor=ffffff"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as r:
            out.write_bytes(r.read())
        return out.stat().st_size > 0
    except Exception as e:
        print(f"    ! Error descargando mermaid: {e}", file=sys.stderr)
        return False


def extract_meta(text: str, fallback_title: str) -> dict:
    title_m = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else fallback_title

    modulo = re.search(r"\*\*M[oó]dulo:\*\*\s*(.+?)\s*(?:<br>|  $|\n|$)", text)
    temas = re.search(r"\*\*Temas?:\*\*\s*(.+?)\s*(?:<br>|  $|\n|$)", text)
    curso = re.search(r"\*\*Curso:\*\*\s*(.+?)\s*(?:<br>|  $|\n|$)", text)
    fecha = re.search(r"\*\*Fecha:?\*\*\s*([^\n_]+?)\s*(?:<br>|  $|\n|$)", text)

    parts = []
    if modulo:
        parts.append(modulo.group(1).strip())
    if temas:
        parts.append(temas.group(1).strip())
    subtitle = " — ".join(parts)

    author = curso.group(1).strip() if curso else ""
    date = ""
    if fecha:
        candidate = fecha.group(1).strip()
        if candidate and "___" not in candidate:
            date = candidate

    return {"title": title, "subtitle": subtitle, "author": author, "date": date}


def yaml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def preprocess(text: str, img_dir: Path) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)

    counter = {"n": 0}

    def repl(m):
        counter["n"] += 1
        code = m.group(1).strip()
        png = img_dir / f"mermaid_{counter['n']}.png"
        if fetch_mermaid_png(code, png):
            return f"\n![Diagrama de red]({png}){{width=80%}}\n"
        return "\n*[Diagrama Mermaid no disponible: comprueba la conexión a mermaid.ink]*\n"

    text = re.sub(r"```mermaid\s*\n(.*?)```", repl, text, flags=re.DOTALL)
    return text


def build_yaml(meta: dict, toc: bool) -> str:
    lines = ["---", f'title: "{yaml_escape(meta["title"])}"']
    if meta["subtitle"]:
        lines.append(f'subtitle: "{yaml_escape(meta["subtitle"])}"')
    if meta["author"]:
        lines.append(f'author: "{yaml_escape(meta["author"])}"')
    if meta["date"]:
        lines.append(f'date: "{yaml_escape(meta["date"])}"')
    lines += [
        "lang: es",
        "papersize: a4",
        "fontsize: 11pt",
        'mainfont: "Helvetica Neue"',
        'monofont: "Menlo"',
        f"toc: {'true' if toc else 'false'}",
    ]
    if toc:
        lines.append("toc-depth: 2")
    lines += [
        "margin-left: 2cm",
        "margin-right: 2cm",
        "margin-top: 2.5cm",
        "margin-bottom: 2.5cm",
        "---",
        "",
        "",
    ]
    return "\n".join(lines)


def count_headings(text: str) -> int:
    return len(re.findall(r"^#{1,3}\s+", text, flags=re.MULTILINE))


def convert_one(md_path: Path) -> bool:
    print(f"\n→ {md_path.name}")
    raw = md_path.read_text(encoding="utf-8")
    meta = extract_meta(raw, fallback_title=md_path.stem)

    out_pdf = EXTRA / (md_path.stem + ".pdf")

    with tempfile.TemporaryDirectory() as tmp:
        img_dir = Path(tmp)
        body = preprocess(raw, img_dir)

        toc_needed = count_headings(body) >= 8
        if toc_needed:
            print("    · TOC: activado")
        full_md = build_yaml(meta, toc_needed) + body

        tmp_md = img_dir / (md_path.stem + ".md")
        tmp_md.write_text(full_md, encoding="utf-8")

        cmd = [
            "pandoc",
            str(tmp_md),
            "-o",
            str(out_pdf),
            "--pdf-engine=typst",
            "--highlight-style=tango",
            "--from=markdown+pipe_tables+grid_tables+yaml_metadata_block+raw_tex",
        ]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print("    ✗ ERROR de Pandoc/Typst:")
            print(r.stderr.strip())
            return False

    size = out_pdf.stat().st_size / 1024
    print(f"    ✓ {out_pdf.name}  ({size:.0f} KB)")
    return True


def resolve_target(arg: str) -> Path:
    p = Path(arg)
    if p.is_absolute():
        return p
    candidates = [Path.cwd() / arg, EXTRA / arg, EXTRA / p.name]
    for c in candidates:
        if c.exists():
            return c
    return EXTRA / arg


def main(argv):
    targets = [resolve_target(a) for a in (argv or DEFAULT_TARGETS)]
    failed = []
    for p in targets:
        if not p.exists():
            print(f"✗ No existe: {p}")
            failed.append(p.name)
            continue
        if not convert_one(p):
            failed.append(p.name)

    if failed:
        print(f"\nFallaron: {failed}")
        sys.exit(1)
    print("\nOK – PDFs generados en", EXTRA)


if __name__ == "__main__":
    main(sys.argv[1:])
