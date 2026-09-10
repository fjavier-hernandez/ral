#!/usr/bin/env python3
"""
Convierte MD de examen a DOCX: reemplaza bloques Mermaid por imágenes (mermaid.ink)
y ejecuta pandoc con documento de referencia.
Uso: python md_to_docx_converter.py <modelo_A|modelo_B>
"""
import re
import sys
import base64
import subprocess
import tempfile
import os
from pathlib import Path

# Directorio del script (Extra/)
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DOCS_DIR = REPO_ROOT / "docs"
EXTRA_DIR = REPO_ROOT / "Extra"


def b64url_encode(s: str) -> str:
    """Base64url encode (sin +/ y sin padding)."""
    b = s.encode("utf-8")
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode("ascii")


def replace_mermaid_with_image(content: str) -> str:
    """Sustituye cada bloque ```mermaid ... ``` por ![Diagrama](https://mermaid.ink/img/...)"""
    def repl(match):
        mermaid_code = match.group(1).strip()
        try:
            encoded = b64url_encode(mermaid_code)
            url = f"https://mermaid.ink/img/{encoded}"
            return f'\n![Diagrama de red]({url})\n'
        except Exception:
            return "\n*[Diagrama Mermaid: generar manualmente]*\n"

    return re.sub(r"```mermaid\s*\n(.*?)```", repl, content, flags=re.DOTALL)


def remove_mkdocs_admonition(content: str) -> str:
    """Convierte !!! warning ... a una nota simple para Word."""
    content = re.sub(
        r'!!!\s*warning\s*"[^"]*"\s*\n\s*(.*?)(?=\n\n|\n---|\Z)',
        r"*Documento interno – no publicar.*\n\n",
        content,
        flags=re.DOTALL,
    )
    return content


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("modelo_A", "modelo_B"):
        print("Uso: python md_to_docx_converter.py modelo_A | modelo_B")
        sys.exit(1)
    model = sys.argv[1]
    md_name = f"Examen_Enrutamiento_Unidad7_Modelo_{model.upper().split('_')[1]}.md"
    ref_docx = DOCS_DIR / f"examen_modelo_{model.split('_')[1].upper()}.docx"
    out_docx = DOCS_DIR / f"Examen_Enrutamiento_Unidad7_Modelo_{model.split('_')[1].upper()}.docx"
    md_path = EXTRA_DIR / md_name

    if not md_path.exists():
        print(f"No se encuentra {md_path}")
        sys.exit(1)

    use_reference = ref_docx.exists()
    if not use_reference:
        print(f"Aviso: no se encuentra {ref_docx}; se generará DOCX sin referencia de estilo.")

    content = md_path.read_text(encoding="utf-8")
    content = remove_mkdocs_admonition(content)
    content = replace_mermaid_with_image(content)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as f:
        f.write(content)
        tmp_md = f.name

    try:
        cmd = ["pandoc", tmp_md, "-o", str(out_docx)]
        if use_reference:
            cmd.append("--reference-doc=" + str(ref_docx))
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print("Pandoc error:", result.stderr)
            sys.exit(1)
        print(f"Generado: {out_docx}")
    finally:
        os.unlink(tmp_md)


if __name__ == "__main__":
    main()
