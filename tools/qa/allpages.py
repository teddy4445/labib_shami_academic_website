from pathlib import Path
from playwright.sync_api import sync_playwright
import os
ROOT = Path(__file__).resolve().parents[2]
AXE_PATH = Path(os.environ.get("AXE_JS", ROOT / "tools/qa/axe.min.js"))

site = ROOT / "site"; pages = sorted(str(p.relative_to(site)) for p in site.rglob('*.html'))
issues = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 320, "height": 800})
    errs = []
    pg.on("pageerror", lambda ex: errs.append(str(ex)))
    pg.on("response", lambda r: errs.append(f"{r.status} {r.url}") if r.status >= 400 else None)
    for path in pages:
        errs.clear()
        pg.goto("http://localhost:8000/" + path, wait_until="networkidle")
        sw = pg.evaluate("() => document.documentElement.scrollWidth")
        h1 = pg.evaluate("() => document.querySelectorAll('h1').length")
        if sw > 321 or errs or h1 != 1: issues.append((path, sw, h1, errs[:2]))
    b.close()
print(len(pages), "pages at 320px;", "issues:", issues)
