# Labib Shami — academic website

A static, content-led academic website for **Dr. Labib Shami**, economist and Senior Researcher at the Taub Center for Social Policy Studies in Israel. The site covers his research on monetary policy, credit, the non-observed economy, SMEs and crisis economics, and his policy analysis for the Taub Center.

- **Deployable folder:** `docs/`, which is plain HTML5, CSS and vanilla JavaScript. GitHub Pages serves it directly from the `main` branch.
- **No build step.** There is no Node, npm, bundler, framework, server code or API key. Copy `docs/` to any static host and it works.
- **Status:** complete and tested (see `research/qa-report.md`). A short list of items awaiting Dr. Shami's sign-off is in **`NEEDS_LABIB_APPROVAL.md`**.

## What's in the repository

```
docs/                         ← the website (GitHub Pages serves this folder)
  index.html                  Home
  research.html               Research themes + full, filterable bibliography
  publications/<slug>/        28 publication landing pages (citation, BibTeX, metadata)
  policy.html                 13 Taub Center reports
  media.html                  Interviews, op-eds, videos, press, talks (original-language titles)
  teaching.html               Teaching, guidebooks, open resources
  404.html  robots.txt  .nojekyll
  css/ js/ fonts/ img/
  data/                       publications.json · publications.bib · policy.json · media.json
tools/
  site_tool.py                Optional helper (Python 3.8+, stdlib only), see "Updating content"
  qa/                         Optional QA: static audit (stdlib) + browser tests (Python Playwright)
research/                     Private: verification, rights, provenance, QA (do not deploy)
  VERIFICATION_AND_RIGHTS.md  What was verified, how, and what may be published
  publications-master.json    Bibliography with sources and verification notes
  …                           identity, reconciliation, site plan, design, brand audit, QA, raw notes
labib-shami-research-pack/    Private: the original research pack (input data)
NEEDS_LABIB_APPROVAL.md       Items only Dr. Shami can decide
```

## Preview locally

```bash
python3 -m http.server 8000 --directory docs
# open http://localhost:8000/
```

Any static server works. Use a server rather than opening files directly (`file://`): the site uses folder-style links such as `publications/<slug>/`, which only a web server resolves to `index.html`.

## Deploy (no build)

### GitHub Pages (set up once)

The website lives in `docs/`, which is one of the two folders GitHub Pages can publish directly. No build and no workflow are needed.

1. Push this repository to GitHub (`git push origin main`).
2. On GitHub, open **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**, set **Branch** to **`main`**, and set the folder to **`/docs`**. Then press **Save**.
4. After a minute or two the site is live at **https://teddy4445.github.io/labib_shami_academic_website/**.

Every later `git push` to `main` updates the live site automatically. Every link is relative, and the site was tested under exactly this kind of sub-path. `docs/.nojekyll` tells GitHub Pages to serve the files as they are, and `docs/404.html` is used for missing pages.

GitHub Pages publishes **only** `docs/`. The other folders (`research/`, `labib-shami-research-pack/`, `tools/`) are not part of the website. Bear in mind, though, that they are still readable on GitHub while the repository is public.

### Custom domain, sitemap and canonical URLs

Once the final address is known:

```bash
python3 tools/site_tool.py --base https://teddy4445.github.io/labib_shami_academic_website/
```

This writes `docs/sitemap.xml` and adds the `Sitemap:` line to `docs/robots.txt`. Use your own domain in place of the address above if you have one. For a custom domain, add it under **Settings → Pages → Custom domain** (GitHub then creates `docs/CNAME`) and configure DNS.

### Other hosts

Upload the **contents** of `docs/` (including the hidden `.nojekyll`) to any static host.

## Updating content

There are two equivalent ways to update the site. Both result in plain static files.

**A. Edit HTML directly.** Every page is readable, hand-written HTML. The header and footer are repeated in each page, so change all of them if you edit navigation. The quickest way is a search-and-replace across `docs/`.

**B. Edit the data and run the helper** (for publications, reports and media):

1. Edit `docs/data/publications.json`, `policy.json` or `media.json`. Copy an existing entry and change the fields. Leave fields empty rather than guessing.
2. Run `python3 tools/site_tool.py`. It validates the data, then rewrites only:
   - the regions between `<!-- BIB:START/END -->` (research.html), `<!-- POLICY:START/END -->` (policy.html) and `<!-- MEDIA:START/END -->` (media.html);
   - the publication pages in `docs/publications/<slug>/`, whose header and footer are copied from research.html;
   - `docs/data/publications.bib`.
3. Preview, then deploy.

`python3 tools/site_tool.py --check` validates the data without writing anything.

### Adding a publication: checklist

- Take the title, authors (in order), venue, volume, issue, pages, dates and DOI from Crossref or the publisher page. Never take them from memory or a file name.
- `type`: `journal-article`, `book-chapter` or `preprint`. `status`: `published`, `online-first` or `preprint`.
- If a preprint later appears in a journal, change the record to the journal version and move the preprint into `versions`. Don't list the same work twice.
- Write the `summary` in your own words from the abstract. Don't paste the publisher's abstract.
- Set `open_access`/`license` only from the publisher's or Crossref's licence information.
- Add a provenance note to `research/publications-master.json` so the record can be checked later.

Home-page highlights (selected papers, latest items) are hand-written in `docs/index.html`, so update them there.

## Quality checks

```bash
python3 tools/site_tool.py --check
python3 tools/qa/audit_static_site.py docs
# optional browser tests (developer machine only): pip install playwright, then serve the site and run
python3 tools/qa/allpages.py        # every page at 320px: overflow, errors, one <h1>
python3 tools/qa/functional.py      # keyboard, menu, filters, no-JS, sub-path, axe-core (if tools/qa/axe.min.js exists)
python3 tools/qa/shots.py           # screenshots at 320–1440px, light and dark
```

## Privacy, rights and licences

- No analytics, trackers, cookies, external fonts or CDNs. YouTube loads only when a visitor presses play (`youtube-nocookie.com`).
- No portraits, publisher PDFs, report figures, logos or press images are included, because reuse rights were not established. See `research/VERIFICATION_AND_RIGHTS.md`.
- Fonts: Newsreader and Source Sans 3, under the SIL Open Font License 1.1 (licence files in `docs/fonts/`).
- Code (HTML, CSS, JS, tools) is under the repository's `LICENSE` (Apache-2.0). Biographical and editorial text © 2026 Labib Shami. Linked articles, reports and media belong to their publishers.
