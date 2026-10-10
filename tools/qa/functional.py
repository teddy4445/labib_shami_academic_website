"""Functional, keyboard, no-JS, subpath and axe-core accessibility checks (dev-only)."""
# Usage: python3 -m http.server 8000 --directory docs  (and, for the subpath test, serve a folder containing a
# symlink named labib_shami_academic_website -> docs on port 8001). Requires: pip install playwright.
# Optional: put axe-core's axe.min.js at tools/qa/axe.min.js (or set AXE_JS) to run the accessibility rules.
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
import os
ROOT = Path(__file__).resolve().parents[2]
AXE_PATH = Path(os.environ.get("AXE_JS", ROOT / "tools/qa/axe.min.js"))


B = "http://localhost:8000/"
SUB = "http://localhost:8001/labib_shami_academic_website/"
AXE = (AXE_PATH.read_text() if AXE_PATH.exists() else "")
PAGES = ["index.html", "research.html", "policy.html", "media.html", "teaching.html", "404.html",
         "publications/2019-dynamic-monetary-equilibrium-non-observed-economy/",
         "publications/2026-un-financing-cooperative-game/"]
results = []

def rec(name, ok, detail=""):
    results.append({"test": name, "result": "pass" if ok else "FAIL", "detail": detail})

with sync_playwright() as p:
    br = p.chromium.launch()

    # 1. Skip link + keyboard focus
    pg = br.new_page(viewport={"width": 1280, "height": 900})
    pg.goto(B + "index.html")
    pg.keyboard.press("Tab")
    a = pg.evaluate("() => [document.activeElement.className, document.activeElement.getBoundingClientRect().top]")
    rec("Skip link is first focusable and becomes visible", a[0] == "skip-link" and a[1] >= 0, str(a))
    pg.keyboard.press("Enter")
    rec("Skip link moves to #main", pg.evaluate("() => location.hash") == "#main")
    # focus ring visible on a nav link
    pg.goto(B + "index.html"); pg.keyboard.press("Tab"); pg.keyboard.press("Tab")
    outline = pg.evaluate("() => getComputedStyle(document.activeElement).outlineStyle + ' ' + getComputedStyle(document.activeElement).outlineWidth")
    rec("Visible focus outline on keyboard focus", "solid" in outline, outline)

    # 2. Mobile menu
    m = br.new_page(viewport={"width": 390, "height": 800})
    m.goto(B + "research.html")
    t = m.locator(".nav-toggle")
    rec("Menu toggle visible on mobile", t.is_visible())
    t.click()
    rec("Menu opens (aria-expanded=true, nav visible)", t.get_attribute("aria-expanded") == "true" and m.locator("#site-nav").is_visible())
    rec("Focus moves into menu", m.evaluate("() => document.activeElement.closest('#site-nav') !== null"))
    m.keyboard.press("Escape")
    rec("Escape closes menu and returns focus", t.get_attribute("aria-expanded") == "false" and m.evaluate("() => document.activeElement.classList.contains('nav-toggle')"))
    t.click(); m.mouse.click(200, 700)
    rec("Click outside closes menu", t.get_attribute("aria-expanded") == "false")

    # 3. Bibliography explorer
    r = br.new_page(viewport={"width": 1280, "height": 900})
    r.goto(B + "research.html")
    count = lambda: r.locator("#bib-count").inner_text()
    vis = lambda: r.evaluate("() => document.querySelectorAll('.bib-entry:not([hidden])').length")
    rec("Bibliography renders all 28 entries", vis() == 28 and "28" in count(), count())
    r.fill("#bib-q", "lazebnik"); r.wait_for_timeout(400)
    n_l = vis(); rec("Search by co-author", 10 < n_l < 28, f"{n_l} – {count()}")
    r.fill("#bib-q", "lazebnik shami pandemic"); r.wait_for_timeout(400)
    n_m = vis(); rec("Multi-term search (AND)", 0 < n_m < n_l, f"{n_m}")
    r.fill("#bib-q", "istrazivanja"); r.wait_for_timeout(400)
    rec("Accent-insensitive search (Istraživanja)", vis() == 1, str(vis()))
    r.fill("#bib-q", "<script>alert(1)</script> \"'&"); r.wait_for_timeout(400)
    rec("Strange characters: no error, empty state shown", vis() == 0 and r.locator("#bib-empty").is_visible())
    r.click("#bib-empty-reset"); r.wait_for_timeout(200)
    rec("Empty-state reset restores all", vis() == 28)
    r.select_option("#bib-type", "preprint"); r.wait_for_timeout(200)
    rec("Type filter: preprints", vis() == 2, str(vis()))
    r.select_option("#bib-type", "book-chapter"); r.wait_for_timeout(200)
    rec("Type filter: book chapter", vis() == 1, str(vis()))
    r.select_option("#bib-type", "all"); r.select_option("#bib-topic", "non-observed"); r.wait_for_timeout(200)
    rec("Theme filter: non-observed", vis() == 7, str(vis()))
    rec("URL reflects filters", "topic=non-observed" in r.url, r.url)
    r.select_option("#bib-topic", "all"); r.select_option("#bib-sort", "oldest"); r.wait_for_timeout(200)
    first = r.evaluate("() => document.querySelector('[data-year-group]:not([hidden])').getAttribute('data-year-group')")
    rec("Sort oldest first", first == "2019", first)
    hidden_groups = r.evaluate("() => [...document.querySelectorAll('[data-year-group]')].filter(g=>g.hidden).length")
    r.click("#bib-reset"); r.wait_for_timeout(200)
    rec("Reset button restores defaults", vis() == 28 and r.input_value("#bib-sort") == "newest")
    r.goto(B + "research.html?topic=crisis&type=journal-article#publications"); r.wait_for_timeout(300)
    rec("Deep link ?topic=crisis preselects filter", r.input_value("#bib-topic") == "crisis" and vis() == 8, str(vis()))

    # 4. Policy and media chips
    pol = br.new_page(viewport={"width": 1280, "height": 900})
    pol.goto(B + "policy.html")
    pol.click("button[data-filter=hidden]")
    v = pol.evaluate("() => document.querySelectorAll('.report[data-filter-item]:not([hidden])').length")
    s = pol.evaluate("() => document.querySelectorAll('[data-filter-section]:not([hidden])').length")
    rec("Policy chip filter (non-observed economy)", v == 1 and s == 1, f"{v} reports, {s} sections")
    rec("Policy chip aria-pressed", pol.get_attribute("button[data-filter=hidden]", "aria-pressed") == "true")
    pol.goto(B + "policy.html?theme=macro")
    v = pol.evaluate("() => document.querySelectorAll('.report[data-filter-item]:not([hidden])').length")
    rec("Policy deep link ?theme=macro", v == 6, str(v))
    med = br.new_page(viewport={"width": 1280, "height": 900})
    med.goto(B + "media.html?type=radio")
    v = med.evaluate("() => document.querySelectorAll('[data-filter-item]:not([hidden])').length")
    rec("Media deep link ?type=radio", v == 2, str(v))
    med.goto(B + "media.html")
    med.click("button[data-youtube]")
    src = med.evaluate("() => (document.querySelector('.video__frame iframe')||{}).src || ''")
    rec("Video facade swaps in youtube-nocookie iframe on click", "youtube-nocookie.com/embed/" in src, src)
    
    # 5. Copy citation
    ctx = br.new_context(viewport={"width": 1280, "height": 900}, permissions=["clipboard-read", "clipboard-write"])
    cp = ctx.new_page(); cp.goto(B + "publications/2019-dynamic-monetary-equilibrium-non-observed-economy/")
    cp.click("button[data-copy-target=cite-apa]"); cp.wait_for_timeout(300)
    clip = cp.evaluate("() => navigator.clipboard.readText()")
    rec("Copy citation to clipboard", clip.startswith("Shami, L. (2019)."), clip[:60])

    # 6. No-JS
    nj = br.new_context(java_script_enabled=False, viewport={"width": 390, "height": 800})
    q = nj.new_page(); q.goto(B + "research.html")
    rec("No-JS: full bibliography visible", q.evaluate("() => 1") if False else q.locator(".bib-entry").count() == 28 and q.locator(".bib-entry").first.is_visible())
    rec("No-JS: filter form hidden (no dead controls)", not q.locator("#bib-controls").is_visible())
    rec("No-JS: navigation links visible on mobile", q.locator("#site-nav a[href='policy.html']").is_visible())
    q.goto(B + "media.html")
    rec("No-JS: media items and outbound links present", q.locator(".media-item").count() >= 10 and q.locator(".video a.ext").count() == 4)

    # 7. Subpath + network log
    sp = br.new_page(viewport={"width": 1280, "height": 900})
    bad, ext = [], []
    sp.on("response", lambda resp: bad.append(f"{resp.status} {resp.url}") if resp.status >= 400 else None)
    sp.on("request", lambda req: ext.append(req.url) if not req.url.startswith("http://localhost") else None)
    for path in PAGES[:-1] + ["publications/2026-un-financing-cooperative-game/"]:
        sp.goto(SUB + path, wait_until="networkidle")
    rec("GitHub Pages subpath: all assets load (no 4xx/5xx)", not [b for b in bad if "404.html" not in b], "; ".join(bad[:5]))
    rec("No third-party requests on page load", not ext, "; ".join(ext[:5]))

    # 8. 200% text zoom
    z = br.new_page(viewport={"width": 1280, "height": 900})
    zo = []
    for path in PAGES[:6]:
        z.goto(B + path); z.evaluate("() => document.documentElement.style.fontSize = '200%'"); z.wait_for_timeout(100)
        sw = z.evaluate("() => document.documentElement.scrollWidth")
        if sw > 1281: zo.append(f"{path}:{sw}")
    rec("200% text size: no horizontal overflow at 1280px", not zo, ", ".join(zo))

    # 9. axe-core (WCAG 2.1 AA rules) light + dark
    for scheme in (("light", "dark") if AXE else ()):
        ax = br.new_context(viewport={"width": 1280, "height": 900}, color_scheme=scheme).new_page()
        for path in PAGES:
            ax.goto(B + path, wait_until="networkidle")
            ax.add_script_tag(content=AXE)
            res = ax.evaluate("async () => { const r = await axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa','best-practice']}}); return r.violations.map(v => ({id: v.id, impact: v.impact, n: v.nodes.length, t: v.nodes.slice(0,3).map(n=>n.target.join(' ')).join(' | ')})); }")
            rec(f"axe {scheme}: {path}", not res, json.dumps(res)[:700])
    br.close()

fails = [r for r in results if r["result"] != "pass"]
for r in results:
    print(f"{r['result']:4}  {r['test']}  {('— ' + r['detail']) if r['detail'] and r['result'] != 'pass' else ''}")
(ROOT / "research/qa/functional-results.json").write_text(json.dumps(results, indent=1, ensure_ascii=False))
print(f"\n{len(results) - len(fails)}/{len(results)} passed")
