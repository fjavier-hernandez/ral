#!/usr/bin/env python3
"""Ajusta tablas de un .docx ya generado por pandoc.

- Ninguna fila se parte entre páginas (w:cantSplit).
- La primera fila se repite como cabecera (w:tblHeader).
- Si la tabla tiene pocas filas, se procura mantenerla junta (keepNext),
  salvo el último párrafo, para que un título no se quede solo y una tabla
  corta no empiece al final de la página. Las tablas largas sí pueden
  pasar de página, con la cabecera repetida y las filas enteras.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
# Tablas de hasta este número de filas se intentan mantener en la misma página.
MAX_ROWS_KEEP_TOGETHER = 8


def ensure_child(parent, tag: str):
    found = parent.find(tag)
    if found is None:
        found = ET.SubElement(parent, tag)
    return found


def tr_pr(tr):
    pr = tr.find(f"{W}trPr")
    if pr is None:
        pr = ET.Element(f"{W}trPr")
        tr.insert(0, pr)
    return pr


def p_pr(p):
    pr = p.find(f"{W}pPr")
    if pr is None:
        pr = ET.Element(f"{W}pPr")
        p.insert(0, pr)
    return pr


def fix_tree(root) -> tuple[int, int]:
    tables = 0
    rows = 0
    for tbl in root.iter(f"{W}tbl"):
        tables += 1
        trs = list(tbl.findall(f"{W}tr"))
        for index, tr in enumerate(trs):
            rows += 1
            pr = tr_pr(tr)
            ensure_child(pr, f"{W}cantSplit")
            if index == 0:
                ensure_child(pr, f"{W}tblHeader")
        if 0 < len(trs) <= MAX_ROWS_KEEP_TOGETHER:
            paragraphs = []
            for tr in trs:
                for p in tr.iter(f"{W}p"):
                    paragraphs.append(p)
            for p in paragraphs[:-1]:
                ensure_child(p_pr(p), f"{W}keepNext")
                ensure_child(p_pr(p), f"{W}keepLines")
    return tables, rows


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Uso: fix_docx_tables.py archivo.docx")
    path = Path(sys.argv[1])
    with zipfile.ZipFile(path, "r") as zin:
        xml = zin.read("word/document.xml")
        others = {name: zin.read(name) for name in zin.namelist() if name != "word/document.xml"}
    root = ET.fromstring(xml)
    tables, rows = fix_tree(root)
    new_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    tmp = path.with_suffix(".docx.tmp")
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in others.items():
            zout.writestr(name, data)
        zout.writestr("word/document.xml", new_xml)
    tmp.replace(path)
    print(f"Tablas ajustadas: {tables}. Filas: {rows}.")


if __name__ == "__main__":
    main()
