# Frozen Meat — website

Static site published with GitHub Pages: https://vahan04.github.io/biubiu/

- `src/template.html` — page source (HTML, CSS, JS, translations). Edit this file.
- `src/build.py` — fills image paths into the template and writes `index.html`.
- `assets/img/` — product and brand images; `assets/fonts/` — self-hosted Noto Sans (Armenian, Latin, Cyrillic).

Build: `python3 src/build.py`, then commit `index.html` together with the source.
