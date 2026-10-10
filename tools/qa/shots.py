"""QA screenshots + overflow/console checks (dev-only; Python Playwright)."""
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
import os
ROOT = Path(__file__).resolve().parents[2]
AXE_PATH = Path(os.environ.get("AXE_JS", ROOT / "tools/qa/axe.min.js"))


BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000/"
OUT = ROOT / "research/qa/screenshots"; OUT.mkdir(parents=True, exist_ok=True)
pages = ["index.html", "research.html", "policy.html", "media.html", "teaching.html",
         "publications/2019-dynamic-monetary-equilibrium-non-observed-economy/", "404.html"]
widths = [320, 390, 768, 1280, 1440]
report = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for scheme in ["light", "dark"]:
        for w in widths:
            ctx = b.new_context(viewport={"width": w, "height": 900}, color_scheme=scheme, device_scale_factor=1)
            pg = ctx.new_page()
            errs = []
            pg.on("console", lambda m: errs.append(f"console.{m.type}: {m.text}") if m.type in ("error", "warning") else None)
            pg.on("pageerror", lambda ex: errs.append(f"pageerror: {ex}"))
            pg.on("requestfailed", lambda r: errs.append(f"failed: {r.url}"))
            pg.on("response", lambda r: errs.append(f"HTTP {r.status}: {r.url}") if r.status >= 400 and "localhost" in r.url else None)
            for path in pages:
                if scheme == "dark" and w not in (390, 1440):
                    continue
                errs.clear()
                pg.goto(BASE + path, wait_until="networkidle")
                pg.wait_for_timeout(150)
                ov = pg.evaluate("""() => { const d = document.documentElement; const over = [];
                    if (d.scrollWidth > window.innerWidth + 1) {
                      for (const el of document.querySelectorAll('body *')) { const r = el.getBoundingClientRect(); if (r.right > window.innerWidth + 1 && r.width > 0) over.push(el.tagName + '.' + (el.className||'').toString().slice(0,40)); }
                    }
                    return {sw: d.scrollWidth, iw: window.innerWidth, over: over.slice(0,8)}; }""")
                name = f"{scheme}-{w}-{path.strip('/').replace('/', '_').replace('.html','') or 'index'}"
                full = w in (390, 1440) and scheme == "light"
                pg.screenshot(path=str(OUT / f"{name}.png"), full_page=full)
                report.append({"page": path, "w": w, "scheme": scheme, "overflow": ov["sw"] > ov["iw"] + 1, "detail": ov, "errors": list(errs)})
            ctx.close()
    b.close()
bad = [r for r in report if r["overflow"] or r["errors"]]
print(json.dumps(bad, indent=1)[:6000])
print("checked", len(report), "page/viewport combos;", len(bad), "with issues")
