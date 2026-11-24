#!/usr/bin/env python3
"""Build index.html from src/template.html. Run from repo root: python3 src/build.py"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = {
    "LOGO": "logo_lat.png", "FMW": "fm_white.png", "FMT": "fm_teal.png", "FARM": "farm.jpg",
    "HEN": "hen.jpg", "PACK": "pack.jpg", "LEGS": "legs.jpg", "WHOLE": "whole.jpg",
    "FILLET": "fillet.jpg", "WING": "wing.jpg", "BONE": "bonebreast.jpg", "SCHN": "schnitzel.jpg",
    "SAUS": "sausage.jpg", "PHAM": "pork_ham.jpg", "PNECK": "pork_neck.jpg", "STICKS": "sticks.jpg",
    "FRY": "frysaus.jpg", "PFAT": "pork_fat.jpg", "NUG": "nuggets2.jpg", "CUT": "cutlet.jpg",
}
html = (ROOT / "src/template.html").read_text(encoding="utf-8")
for key, name in IMAGES.items():
    path = ROOT / "assets/img" / name
    if not path.exists():
        raise SystemExit(f"missing image: {path}")
    html = html.replace("{{%s}}" % key, f"assets/img/{name}")
left = re.findall(r"\{\{\w+\}\}", html)
if left:
    raise SystemExit(f"unreplaced placeholders: {sorted(set(left))}")
(ROOT / "index.html").write_text(html, encoding="utf-8")
print(f"index.html: {len(html.encode())//1024} KB")
