# QA report (10 October 2026)

Environment: local preview with `python3 -m http.server` (root on :8000, and a GitHub-Pages-style subpath `/labib_shami_academic_website/` on :8001). Browser: headless Chromium 1194 via Python Playwright. Scripts: `tools/qa/shots.py`, `tools/qa/functional.py`, `tools/qa/allpages.py`. Raw results: `research/qa/functional-results.json`. Screenshots: `research/qa/screenshots/`.

## Automated checks

| Test | Method | Result |
|---|---|---|
| Static structure, local links, assets, duplicate IDs, `href` safety | Kit script `audit_static_site.py site` | **Pass.** 35 pages, 0 errors. Two expected warnings: no `sitemap.xml` (domain unknown) and 404 page set to `noindex` (intended). |
| HTML5 + CSS validity | Nu Html Checker (vnu.jar 26.10.9) `--also-check-css` on all 35 pages | **Pass.** No errors. |
| JSON / JSON-LD syntax | Python `json` on `data/*.json` and every `application/ld+json` block | **Pass** |
| Data integrity | `python3 tools/site_tool.py --check` (unique slugs/DOIs, DOI format, Shami in every author list, valid types) | **Pass** |
| Bibliographic accuracy | Every DOI-backed record (26) compared field by field with its live Crossref record (author list and order, volume, issue, pages), in the in-app browser on 10 Oct 2026 | **Pass**, 26/26 match. The 2 preprints were checked against arXiv/SSRN. |
| Horizontal overflow | All 35 pages at 320px; 8 key pages at 320/390/768/1280/1440 (light) and 390/1440 (dark) | **Pass** after fixes (see below) |
| Console errors, page errors, 4xx/5xx | Logged during all of the runs above | **Pass**, none |
| Exactly one `<h1>` per page | All 35 pages | **Pass** |
| Accessibility rules | axe-core 4.10.2 (WCAG 2.0/2.1 A + AA + best-practice) on 9 representative pages × light/dark | **Pass**, 0 violations |
| Skip link | Tab once → visible "Skip to content", Enter → `#main` | **Pass** |
| Visible focus | `:focus-visible` outline on nav links | **Pass** |
| Mobile menu | Opens with `aria-expanded=true`, focus moves into menu, Escape closes and returns focus, outside click closes | **Pass** |
| Bibliography: no filter / co-author / multi-term AND / accent-insensitive ("istrazivanja" → Istraživanja) / script & quote characters → empty state / empty-state reset / type = preprint (2) / chapter (1) / theme = non-observed (7) / URL sync / sort oldest-first / reset / deep link `?topic=crisis&type=journal-article` (8) | Playwright | **Pass** (all) |
| Policy chip filter and `?theme=macro` (6) | Playwright | **Pass** |
| Media `?type=radio` (2) | Playwright | **Pass** |
| Video facade | Click → `youtube-nocookie.com/embed/…` iframe | **Pass** |
| No third-party requests on load | Network log on 9 pages (including media.html) | **Pass**, 0 non-local requests |
| Copy citation | Clipboard read after click | **Pass** |
| JavaScript disabled | Full bibliography (28) visible; filter form hidden; mobile nav links visible; media links present | **Pass** |
| GitHub Pages subpath | All pages and assets under `/labib_shami_academic_website/` | **Pass**, no 4xx |
| 200% text size | Root font-size 200% at 1280px on 6 main pages | **Pass**, no overflow |
| Python helper compatibility | `py_compile`, plus a tokenizer check for f-string constructs that need Python ≥3.12 | **Pass**. Written for Python 3.8+. |

## Defects found and fixed during QA

1. Paper pages overflowed by 50px at 320–1280px. A long unbreakable DOI widened an implicit grid track in the aside. Fixed with `grid-template-columns: minmax(0,1fr)` and `overflow-wrap:anywhere` on `dd`.
2. Hero name line: the "·" separator rendered after the Arabic name because of bidi ordering. Fixed with an explicit separator element.
3. Eyebrow rule wrapped awkwardly on mobile in the hero. Fixed by removing the rule on that eyebrow.
4. Hero diagram labels were too small at 390px. On small screens the sub-labels are now hidden, the labels enlarged and the label positions nudged so they don't sit on the curves.
5. The Arabic timeline link put its ↗ marker at the wrong end. Fixed by isolating the RTL text inside an LTR link.
6. The timeline was out of date order. Fixed.
7. Wording fixes from the claim audit (see `brand-audit.md`).

## Manual review (from screenshots)

Home, Research, a paper page, Policy, Media, Teaching and About were reviewed at desktop and mobile widths in light mode, and Home and Media in dark mode. Hierarchy, line lengths, card rhythm, RTL titles and the contact band all read correctly.

## Not tested / limits

- No real-device testing (iOS Safari, Android Chrome) and no Firefox. Only Chromium was used.
- No screen-reader session (NVDA/VoiceOver). axe-core and the semantic structure are proxies, not a substitute.
- Outbound links were opened during research rather than by an automated link checker, because the sandbox network blocks most external hosts. Re-check them before launch (`VERIFICATION_AND_RIGHTS.md` §7).
- Core Web Vitals were not measured. Page weight is small: about 15–70 KB of HTML per page, 36 KB of CSS and 10 KB of JS. Fonts are 0.3–0.5 MB, loaded only for the glyph ranges and styles a page uses, and cached after the first visit.
- `og:image`, canonical URLs and `sitemap.xml` are deliberately absent until a production domain is chosen.

## Visual quality rubric (self-assessed, 0–2 each)

| Criterion | Score | Note |
|---|---|---|
| One-sentence research identity above the fold | 2 | |
| Editorial design, not a template | 2 | |
| Concrete, verified, explorable evidence | 2 | |
| Coherent themes | 2 | |
| Meaningful visual anchors | 1 | Original diagram only. No portrait or paper figures (rights). |
| Navigation by audience | 2 | |
| Consistent, accessible colour/components | 2 | |
| Intentional mobile experience | 2 | |
| Scholarly detail pages and filters | 2 | |
| Real, unambiguous actions | 2 | |
| **Total** | **19 / 20** | Adding an approved portrait or author-cleared figures would close the remaining gap. |
