#!/usr/bin/env python3
"""Build index.html from src/template.html. Run from repo root: python3 src/build.py"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = {
    "LOGO": "logo_lat.png", "FMW": "fm_white.png", "FMT": "fm_teal.png", "FARM": "farm_warm.jpg",
    "HEN": "hen.jpg", "PACK": "pack_framed.jpg", "LEGS": "thigh_boneless.jpg", "WHOLE": "whole_framed.jpg",
    "FILLET": "fillet.jpg", "WING": "wing_v2.jpg", "BONE": "bonebreast.jpg", "SCHN": "schnitzel.jpg",
    "SAUS": "sausage.jpg", "PHAM": "pork_ham.jpg", "PNECK": "pork_neck2.jpg", "STICKS": "sticks.jpg",
    "FRY": "frysaus.jpg", "PFAT": "pork_fat.jpg", "NUG": "nuggets2.jpg", "CUT": "cutlet.jpg", "DRUM": "drumstick2.jpg", "PRIB": "pork_ribs_v2.jpg", "PMAT": "pork_matter_v3.jpg", "SPEC": "saus_special.jpg", "LEGQ": "leg_quarter.jpg", "LGMG": "lg_mg.png", "LGZOVQ": "lg_zovq.png", "LGTITAN": "lg_titan.png", "LGINESSA": "lg_inessa.png", "LGCARR": "lg_carrefour.png", "SMOK": "smoked_breast.jpg", "MOOD1": "mood1.jpg", "MOOD2": "mood2.jpg", "MOOD3": "mood3.jpg", "MOOD4": "mood4.jpg", "MOOD5": "mood5.jpg", "MOOD6": "mood6.jpg", "SMLEG": "smoked_leg.jpg", "SMSTK": "smoked_sticks.jpg",
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
