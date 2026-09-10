#!/usr/bin/env python3
"""
Convierte bloques Mermaid (flowchart con subgraphs) a SVG mediante Graphviz.
No modifica los Markdown originales: genera SVG en media/ y devuelve Markdown procesado.

Uso interno para la cadena Markdown → DOCX con Pandoc.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path


def _escape_dot(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def mermaid_flowchart_to_dot(code: str) -> str:
    """Interpreta un flowchart Mermaid con subgraphs y genera DOT equivalente."""
    lines = [ln.strip() for ln in code.strip().splitlines() if ln.strip()]

    rankdir = "LR"
    if lines and lines[0].lower().startswith("flowchart"):
        parts = lines[0].split()
        if len(parts) > 1:
            rankdir = parts[1].upper()

    subgraphs: dict[str, dict] = {}
    stack: list[str] = []
    edges: list[tuple[str, str]] = []

    re_subgraph = re.compile(
        r'^subgraph\s+(\w+)\s*\[\s*"([^"]+)"\s*\]|^subgraph\s+(\w+)\s*\[\s*([^\]]+)\s*\]',
        re.I,
    )
    re_node_quoted = re.compile(r'^(\w+)\s*\[\s*"([^"]+)"\s*\]')
    re_node_plain = re.compile(r'^(\w+)\s*\[\s*([^\]]+)\s*\]')
    re_edge = re.compile(r'^(\w+)\s*[-.]{2,}>?\s*(\w+)\s*$')

    for line in lines[1:]:
        low = line.lower()
        if low.startswith("direction"):
            continue
        if low == "end":
            if stack:
                stack.pop()
            continue

        m = re_subgraph.match(line)
        if m:
            sg_id = m.group(1) or m.group(3)
            sg_label = (m.group(2) or m.group(4) or "").strip()
            subgraphs[sg_id] = {"label": sg_label.strip(), "nodes": []}
            stack.append(sg_id)
            continue

        m = re_node_quoted.match(line) or re_node_plain.match(line)
        if m:
            nid, nlabel = m.group(1), m.group(2).strip()
            if stack:
                subgraphs[stack[-1]]["nodes"].append((nid, nlabel))
            continue

        m = re_edge.match(line)
        if m:
            edges.append((m.group(1), m.group(2)))

    dot: list[str] = [
        "digraph G {",
        f"  rankdir={rankdir};",
        '  bgcolor="white";',
        "  graph [fontname=Helvetica, fontsize=11, splines=ortho, nodesep=0.55, ranksep=0.9];",
        '  node [shape=box, style="rounded,filled", fillcolor="#eef0ff", '
        'color="#5c6bc0", fontname=Helvetica, fontsize=10, margin="0.18,0.10"];',
        '  edge [color="#444444", penwidth=1.3, arrowsize=0.7];',
    ]

    for sg_id, sg in subgraphs.items():
        dot.append(f"  subgraph cluster_{sg_id} {{")
        dot.append(f'    label="{_escape_dot(sg["label"])}";')
        dot.append(
            '    style="rounded,filled"; fillcolor="#fffbf0"; color="#c9a227"; '
            "fontname=Helvetica; fontsize=11; labeljust=l;"
        )
        for nid, nlabel in sg["nodes"]:
            dot.append(f'    {nid} [label="{_escape_dot(nlabel)}"];')
        dot.append("  }")

    def resolve(node_or_subgraph: str) -> tuple[str, str | None]:
        if node_or_subgraph in subgraphs and subgraphs[node_or_subgraph]["nodes"]:
            rep = subgraphs[node_or_subgraph]["nodes"][0][0]
            return rep, f"cluster_{node_or_subgraph}"
        return node_or_subgraph, None

    for src, dst in edges:
        dst_node, lhead = resolve(dst)
        if lhead:
            dot.append(f"  {src} -> {dst_node} [lhead={lhead}];")
        else:
            dot.append(f"  {src} -> {dst_node};")

    dot.append("}")
    return "\n".join(dot)


def render_mermaid_to_svg(code: str, svg_path: Path) -> None:
    """Genera SVG con Graphviz a partir de código Mermaid."""
    dot_src = mermaid_flowchart_to_dot(code)
    dot_path = svg_path.with_suffix(".dot")
    dot_path.write_text(dot_src, encoding="utf-8")
    result = subprocess.run(
        ["dot", "-Tsvg", str(dot_path), "-o", str(svg_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Graphviz dot falló:\n{result.stderr}\n\nDOT:\n{dot_src}")
    if not svg_path.exists() or svg_path.stat().st_size == 0:
        raise RuntimeError(f"SVG no generado: {svg_path}")


def replace_mermaid_blocks(content: str, media_dir: Path, media_rel_prefix: Path) -> str:
    """Sustituye ```mermaid``` por imágenes SVG (Graphviz)."""
    media_dir.mkdir(parents=True, exist_ok=True)
    counter = {"n": 0}

    def repl(match: re.Match) -> str:
        counter["n"] += 1
        code = match.group(1).strip()
        svg_name = f"diagram_{counter['n']}.svg"
        svg_path = media_dir / svg_name
        render_mermaid_to_svg(code, svg_path)
        rel = (media_rel_prefix / svg_name).as_posix()
        return f'\n![Diagrama de red]({rel})\n'

    return re.sub(r"```mermaid\s*\n(.*?)```", repl, content, flags=re.DOTALL)
