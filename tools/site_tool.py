#!/usr/bin/env python3
"""Optional authoring helper for the Labib Shami website (Python 3.8+, standard library only).

The website in ../site is plain static HTML and needs NO build step to be viewed or deployed.
This helper exists only to save typing when the curated data changes. It:

  1. re-renders the regions between <!-- BIB:START --> / <!-- BIB:END --> in site/research.html,
     <!-- POLICY:START --> / <!-- POLICY:END --> in site/policy.html and
     <!-- MEDIA:START --> / <!-- MEDIA:END --> in site/media.html from site/data/*.json;
  2. (re)writes one landing page per publication: site/publications/<slug>/index.html;
  3. writes site/data/publications.bib;
  4. optionally writes site/sitemap.xml when you pass --base https://your.domain/path/

Everything outside the marker regions is hand-written HTML and is never touched.

Usage:
    python3 tools/site_tool.py            # update data-driven regions and paper pages
    python3 tools/site_tool.py --check    # validate data only, write nothing
    python3 tools/site_tool.py --base https://example.org/   # also write sitemap.xml + robots Sitemap line
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DATA = SITE / "data"
ME = "Labib Shami"

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
TYPE_LABEL = {"journal-article": "Journal article", "book-chapter": "Book chapter", "preprint": "Preprint / working paper"}
STATUS_LABEL = {"published": "Published", "online-first": "Online first", "preprint": "Preprint"}
RELATED_POLICY = {
    "money-credit": ["taub-013", "taub-006", "taub-001"],
    "non-observed": ["taub-012"],
    "crisis": ["taub-011"],
}

e = lambda s: html.escape(str(s), quote=True)


# ---------------------------------------------------------------- helpers
def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def fmt_date(iso: str) -> str:
    """'2026-07-07' -> '7 July 2026'; '2025-06' -> 'June 2025'; '2025' -> '2025'."""
    if not iso:
        return ""
    parts = iso.split("-")
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return f"{MONTHS[int(parts[1]) - 1]} {parts[0]}"
    return f"{int(parts[2])} {MONTHS[int(parts[1]) - 1]} {parts[0]}"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s-]", " ", s)).strip()


def family(name: str) -> str:
    return name.split()[-1]


def initials(name: str) -> str:
    given = name.split()[:-1]
    return " ".join(g[0] + "." for g in given)


def authors_html(authors: list[str]) -> str:
    out = []
    for a in authors:
        out.append(f'<span class="me">{e(a)}</span>' if a == ME else e(a))
    if len(out) <= 2:
        return " and ".join(out)
    return ", ".join(out[:-1]) + " and " + out[-1]


def venue_bits(p: dict) -> str:
    bits = ""
    if p.get("volume"):
        bits += f' {e(p["volume"])}'
        if p.get("issue"):
            bits += f'({e(p["issue"])})'
    if p.get("pages"):
        bits += f', {e(p["pages"])}'
    return bits


def citation_apa(p: dict) -> str:
    names = [f"{family(a)}, {initials(a)}" for a in p["authors"]]
    if len(names) == 1:
        au = names[0]
    elif len(names) == 2:
        au = f"{names[0]}, &amp; {names[1]}"
    else:
        au = ", ".join(names[:-1]) + f", &amp; {names[-1]}"
    au = au.replace("&amp;", "&")
    title = p["title"]
    venue = p["venue"]
    tail = ""
    if p["type"] == "book-chapter":
        tail = f" In {venue}" + (f" (pp. {p['pages']})" if p.get("pages") else "") + "."
        venue_part = ""
    else:
        venue_part = f" {venue}"
        if p.get("volume"):
            venue_part += f", {p['volume']}" + (f"({p['issue']})" if p.get("issue") else "")
        if p.get("pages"):
            venue_part += f", {p['pages']}"
        venue_part += "."
    doi = f" https://doi.org/{p['doi']}" if p.get("doi") else ""
    if p["type"] == "book-chapter":
        return f"{au} ({p['year']}). {title}.{tail}{doi}"
    if p["status"] == "online-first":
        return f"{au} ({p['year']}). {title}.{venue_part} Advance online publication.{doi}"
    return f"{au} ({p['year']}). {title}.{venue_part}{doi}"


def bib_escape(s: str) -> str:
    return s.replace("&", r"\&").replace("%", r"\%").replace("–", "--").replace("—", "---")


def bibtex(p: dict) -> str:
    first = norm(family(p["authors"][0])).replace(" ", "").replace("-", "")
    word = next((w for w in norm(p["title"]).split() if len(w) > 3 and w not in {"with", "from", "the", "towards", "using", "tell"}), "work")
    key = f"{first}{p['year']}{word}"
    authors = " and ".join(f"{family(a)}, {' '.join(a.split()[:-1])}" for a in p["authors"])
    fields = [("author", authors), ("title", "{" + bib_escape(p["title"]) + "}"), ("year", str(p["year"]))]
    if p["type"] == "journal-article":
        kind = "article"
        fields.append(("journal", bib_escape(p["venue"])))
        if p.get("volume"):
            fields.append(("volume", p["volume"]))
        if p.get("issue"):
            fields.append(("number", p["issue"]))
        if p.get("pages"):
            fields.append(("pages", bib_escape(p["pages"])))
    elif p["type"] == "book-chapter":
        kind = "incollection"
        fields += [("booktitle", "Handbook of Labor, Human Resources and Population Economics"),
                   ("editor", "Zimmermann, Klaus F."), ("publisher", "Springer"), ("address", "Cham")]
        if p.get("pages"):
            fields.append(("pages", bib_escape(p["pages"])))
    else:
        kind = "misc"
        if "arxiv" in p.get("url", ""):
            fields += [("eprint", p["url"].rsplit("/", 1)[-1]), ("archiveprefix", "arXiv")]
            fields.append(("howpublished", "arXiv preprint"))
        else:
            fields.append(("howpublished", bib_escape(p["venue"])))
    if p.get("doi"):
        fields.append(("doi", p["doi"]))
    body = ",\n".join(f"  {k} = {{{v}}}" if not v.startswith("{") else f"  {k} = {v}" for k, v in fields)
    return f"@{kind}{{{key},\n{body}\n}}"


def badges(p: dict) -> str:
    out = []
    if p["type"] == "preprint":
        out.append('<span class="badge badge--pre">Preprint</span>')
    elif p["type"] == "book-chapter":
        out.append('<span class="badge badge--chapter">Book chapter</span>')
    if p["status"] == "online-first":
        out.append('<span class="badge badge--online">Online first</span>')
    if p.get("open_access") and p["type"] != "preprint":
        out.append('<span class="badge badge--oa">Open access</span>')
    return "".join(out)


# ---------------------------------------------------------------- bibliography
def render_bibliography(pubs: list[dict], themes: dict) -> str:
    years = sorted({p["year"] for p in pubs}, reverse=True)
    out = []
    for y in years:
        group = [p for p in pubs if p["year"] == y]
        group.sort(key=lambda p: (p.get("date_online") or p.get("date_issue") or ""), reverse=True)
        out.append(f'<section class="bib-group" data-year-group="{y}" aria-labelledby="y{y}">')
        out.append(f'  <h3 class="bib-year" id="y{y}">{y}</h3>')
        out.append('  <ol class="bib-list" reversed>')
        for p in group:
            search = norm(" ".join([p["title"], " ".join(p["authors"]), p["venue"], p.get("summary", ""), str(p["year"]),
                                    " ".join(themes.get(t, t) for t in p["themes"]), TYPE_LABEL[p["type"]]]))
            links = [f'<a href="{e(p["page_url"])}">Summary &amp; citation</a>']
            if p.get("doi"):
                links.append(f'<a class="ext" href="https://doi.org/{e(p["doi"])}" rel="noopener">DOI</a>')
            if p.get("url") and "doi.org" not in p["url"]:
                label = "Read on arXiv" if "arxiv.org" in p["url"] else "Publisher page"
                links.append(f'<a class="ext" href="{e(p["url"])}" rel="noopener">{label}</a>')
            for v in p.get("versions", []):
                links.append(f'<a class="ext" href="{e(v["url"])}" rel="noopener">Preprint version</a>')
            tags = badges(p)
            out.append(
                f'    <li class="bib-entry" id="pub-{e(p["slug"])}" data-type="{e(p["type"])}" data-themes="{e(" ".join(p["themes"]))}" '
                f'data-year="{p["year"]}" data-date="{e(p.get("date_online") or p.get("date_issue") or str(p["year"]))}" data-search="{e(search)}">\n'
                + (f'      <div class="bib-entry__tags">{tags}</div>\n' if tags else "")
                + f'      <h4 class="bib-entry__title"><a href="{e(p["page_url"])}">{e(p["title"])}</a></h4>\n'
                f'      <p class="bib-entry__authors">{authors_html(p["authors"])}</p>\n'
                f'      <p class="bib-entry__venue"><span class="venue">{e(p["venue"])}</span>{venue_bits(p)}</p>\n'
                f'      <p class="bib-entry__links">{" ".join(links)}</p>\n'
                f'    </li>')
        out.append("  </ol>")
        out.append("</section>")
    return "\n".join(out)


# ---------------------------------------------------------------- policy
def render_policy(data: dict) -> str:
    out = []
    for key, label in data["themes"].items():
        items = sorted([r for r in data["reports"] if r["theme"] == key], key=lambda r: r["date"], reverse=True)
        if not items:
            continue
        out.append(f'<section class="policy-group section--tight" data-filter-section aria-labelledby="t-{key}">')
        out.append(f'  <h2 id="t-{key}" class="policy-group__title">{e(label)}</h2>')
        out.append('  <div class="report-grid">')
        for r in items:
            au = authors_html(r["authors"]) + (", et al." if r.get("authors_etal") else "")
            series = f' · <span class="report__series">{e(r["series"])}</span>' if r.get("series") else ""
            out.append(
                f'    <article class="report" id="{e(r["id"])}" data-filter-item data-tags="{e(key)}">\n'
                f'      <p class="report__date"><time datetime="{e(r["date"])}">{e(fmt_date(r["date"]))}</time>{series}</p>\n'
                f'      <h3><a href="{e(r["url"])}" rel="noopener">{e(r["title"])}</a></h3>\n'
                f'      <p class="report__authors">{au}</p>\n'
                f'      <p class="report__summary">{e(r["summary"])}</p>\n'
                f'      <p class="report__links"><a class="ext" href="{e(r["url"])}" rel="noopener">Taub Center page</a>'
                f'<a class="ext" href="{e(r["pdf"])}" rel="noopener">PDF</a>'
                f'<a class="ext" href="{e(r["url_he"])}" hreflang="he" lang="he" dir="rtl" rel="noopener">בעברית</a></p>\n'
                f'    </article>')
        out.append("  </div>")
        out.append("</section>")
    return "\n".join(out)


# ---------------------------------------------------------------- media
def video_card(m: dict) -> str:
    lang = m["lang"]
    d = ' dir="rtl"' if lang in ("he", "ar") else ""
    gloss = f'<p class="media-item__gloss">{e(m["gloss"])}</p>' if m.get("gloss") and lang != "en" else ""
    return (
        f'<article class="video" data-filter-item data-tags="{e(m["kind"])}">\n'
        f'  <div class="video__frame">\n'
        f'    <button type="button" class="video__play" data-youtube="{e(m["youtube"])}" data-title="{e(m["title"])}" aria-label="Play video: {e(m["title"])} (loads YouTube)">\n'
        f'      <span class="play-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M6 4l15 8-15 8z"/></svg></span>\n'
        f'      <span class="play-text">Play video</span>\n'
        f'      <span class="play-note">Loads the YouTube player (youtube-nocookie.com) only after you press play.</span>\n'
        f'    </button>\n'
        f'  </div>\n'
        f'  <div class="video__body">\n'
        f'    <p class="media-item__outlet"><time datetime="{e(m["date"])}">{e(fmt_date(m["date"]))}</time> · {e(m["outlet"])}</p>\n'
        f'    <h3 lang="{lang}"{d}>{e(m["title"])}</h3>\n'
        f'    {gloss}\n'
        f'    <p><a class="ext" href="{e(m["url"])}" rel="noopener">Watch on YouTube</a> · {e(m["role"])}</p>\n'
        f'  </div>\n'
        f'</article>')


ACTION = {"radio": "Listen", "press": "Read article", "opinion": "Read op-ed", "talk": "Details", "video": "Watch"}


def media_row(m: dict) -> str:
    lang = m["lang"]
    d = ' dir="rtl"' if lang in ("he", "ar") else ""
    gloss = f'\n      <p class="media-item__gloss">{e(m["gloss"])}</p>' if m.get("gloss") and lang != "en" else (
        f'\n      <p class="muted" style="margin:0">{e(m["gloss"])}</p>' if m.get("gloss") else "")
    prog = f' · <span lang="{lang}"{d}>{e(m["program"])}</span>' if m.get("program") else ""
    return (
        f'  <li class="media-item" data-filter-item data-tags="{e(m["kind"])}">\n'
        f'    <p class="media-item__date"><time datetime="{e(m["date"])}">{e(fmt_date(m["date"]))}</time><span class="media-item__kind">{e(m["role"])}</span></p>\n'
        f'    <div>\n'
        f'      <p class="media-item__outlet">{e(m["outlet"])}{prog}</p>\n'
        f'      <p class="media-item__title" lang="{lang}"{d}>{e(m["title"])}</p>{gloss}\n'
        f'    </div>\n'
        f'    <p class="media-item__action"><a class="ext" href="{e(m["url"])}" rel="noopener">{ACTION.get(m["kind"], "Open")}<span class="visually-hidden">: {e(m["title"])}</span></a></p>\n'
        f'  </li>')


def render_media(data: dict) -> str:
    items = sorted(data["items"], key=lambda m: m["date"], reverse=True)
    out = []
    order = ["video", "radio", "opinion", "press", "talk"]
    for kind in order:
        group = [m for m in items if m["kind"] == kind]
        if not group:
            continue
        label = data["kinds"][kind]
        out.append(f'<section class="section--tight media-group" data-filter-section aria-labelledby="k-{kind}">')
        out.append(f'  <h2 id="k-{kind}">{e(label)}</h2>')
        if kind == "video":
            out.append('  <div class="video-grid">')
            out += ["  " + line for c in group for line in video_card(c).split("\n")]
            out.append("  </div>")
        else:
            out.append('  <ul class="media-list">')
            out += [media_row(m) for m in group]
            out.append("  </ul>")
        out.append("</section>")
    return "\n".join(out)


# ---------------------------------------------------------------- paper pages
def nested(fragment: str, prefix: str = "../../") -> str:
    def fix(m):
        attr, q, url = m.group(1), m.group(2), m.group(3)
        if re.match(r"^(https?:|mailto:|tel:|#|/|data:)", url):
            return m.group(0)
        return f"{attr}={q}{prefix}{url}"
    return re.sub(r'\b(href|src)=(["\'])([^"\']*)', fix, fragment)


def extract(page: str, name: str) -> str:
    m = re.search(rf"<!-- {name}:START -->(.*?)<!-- {name}:END -->", page, re.S)
    if not m:
        raise SystemExit(f"Marker {name} not found in research.html")
    return m.group(1)


def paper_page(p: dict, pubs: list[dict], themes: dict, policy: dict, header: str, footer: str) -> str:
    desc = p["summary"]
    if len(desc) > 158:
        desc = desc[:155].rsplit(" ", 1)[0] + "…"
    meta = [f'<meta name="citation_title" content="{e(p["title"])}">']
    meta += [f'<meta name="citation_author" content="{e(a)}">' for a in p["authors"]]
    date = (p.get("date_issue") or p.get("date_online") or str(p["year"])).replace("-", "/")
    meta.append(f'<meta name="citation_publication_date" content="{e(date)}">')
    if p.get("date_online"):
        meta.append(f'<meta name="citation_online_date" content="{e(p["date_online"].replace("-", "/"))}">')
    if p["type"] == "journal-article":
        meta.append(f'<meta name="citation_journal_title" content="{e(p["venue"])}">')
        if p.get("volume"):
            meta.append(f'<meta name="citation_volume" content="{e(p["volume"])}">')
        if p.get("issue"):
            meta.append(f'<meta name="citation_issue" content="{e(p["issue"])}">')
        if p.get("pages"):
            pg = re.split(r"[–-]", p["pages"])
            meta.append(f'<meta name="citation_firstpage" content="{e(pg[0])}">')
            if len(pg) > 1:
                meta.append(f'<meta name="citation_lastpage" content="{e(pg[1])}">')
    elif p["type"] == "book-chapter":
        meta.append('<meta name="citation_inbook_title" content="Handbook of Labor, Human Resources and Population Economics">')
        meta.append('<meta name="citation_publisher" content="Springer">')
    else:
        meta.append(f'<meta name="citation_technical_report_institution" content="{e(p["venue"])}">')
    if p.get("doi"):
        meta.append(f'<meta name="citation_doi" content="{e(p["doi"])}">')
    ld = {
        "@context": "https://schema.org",
        "@type": "Chapter" if p["type"] == "book-chapter" else "ScholarlyArticle",
        "headline": p["title"][:110], "name": p["title"],
        "author": [{"@type": "Person", "name": a} for a in p["authors"]],
        "datePublished": p.get("date_online") or p.get("date_issue") or str(p["year"]),
        "description": p["summary"],
        "isPartOf": {"@type": "Periodical" if p["type"] == "journal-article" else "CreativeWork", "name": p["venue"]},
        "about": [themes[t] for t in p["themes"]],
    }
    if p.get("doi"):
        ld["identifier"] = {"@type": "PropertyValue", "propertyID": "DOI", "value": p["doi"]}
        ld["sameAs"] = f"https://doi.org/{p['doi']}"
    if p.get("open_access") and p.get("license", "").startswith("CC"):
        ld["license"] = {"CC BY 4.0": "https://creativecommons.org/licenses/by/4.0/", "CC BY-NC 4.0": "https://creativecommons.org/licenses/by-nc/4.0/"}.get(p["license"], p["license"])
    ld_json = json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")

    primary = p["url"] or (f"https://doi.org/{p['doi']}" if p.get("doi") else "")
    plabel = "Read on arXiv" if "arxiv.org" in primary else ("Read on SSRN" if "ssrn" in primary else "Read the article")
    buttons = [f'<a class="btn btn--primary ext" href="{e(primary)}" rel="noopener">{plabel}</a>']
    for v in p.get("versions", []):
        buttons.append(f'<a class="btn btn--ghost ext" href="{e(v["url"])}" rel="noopener">{e(v["label"])}</a>')

    dl = [("Type", TYPE_LABEL[p["type"]]), ("Status", STATUS_LABEL[p["status"]])]
    if p["type"] != "book-chapter":
        dl.append(("Venue", f'<span class="venue">{e(p["venue"])}</span>'))
    else:
        dl.append(("In", e(p["venue"])))
    if p.get("volume"):
        dl.append(("Volume", e(p["volume"]) + (f' · Issue {e(p["issue"])}' if p.get("issue") else "")))
    if p.get("pages"):
        dl.append(("Pages" if re.search(r"[–-]", p["pages"]) else "Article no.", e(p["pages"])))
    if p.get("date_online"):
        dl.append(("Online", e(fmt_date(p["date_online"]))))
    if p.get("date_issue"):
        dl.append(("Issue date", e(fmt_date(p["date_issue"]))))
    if p.get("doi"):
        dl.append(("DOI", f'<a href="https://doi.org/{e(p["doi"])}" rel="noopener">{e(p["doi"])}</a>'))
    if p["type"] == "preprint":
        dl.append(("Access", "Freely available preprint"))
    elif p.get("open_access"):
        dl.append(("Access", "Open access" + (f" · {e(p['license'])}" if p.get("license", "").startswith("CC") else "")))
    else:
        dl.append(("Access", "Publisher’s version; may require a subscription"))
    dl_html = "\n".join(f"            <dt>{k}</dt><dd>{v}</dd>" for k, v in dl)

    related = [q for q in pubs if q["id"] != p["id"] and set(q["themes"]) & set(p["themes"])]
    related.sort(key=lambda q: (-len(set(q["themes"]) & set(p["themes"])), -q["year"]))
    rel_html = "\n".join(
        f'          <li><a href="../{e(q["slug"])}/">{e(q["title"])}</a> <span class="muted">· {e(q["venue"])}, {q["year"]}</span></li>'
        for q in related[:4])
    pol_ids = []
    for t in p["themes"]:
        for rid in RELATED_POLICY.get(t, []):
            if rid not in pol_ids:
                pol_ids.append(rid)
    reports = {r["id"]: r for r in policy["reports"]}
    pol_html = "\n".join(
        f'          <li><a class="ext" href="{e(reports[rid]["url"])}" rel="noopener">{e(reports[rid]["title"])}</a> <span class="muted">· Taub Center, {reports[rid]["year"]}</span></li>'
        for rid in pol_ids[:3] if rid in reports)
    theme_links = " ".join(
        f'<a class="chip" href="../../research.html?topic={e(t)}#publications">{e(themes[t])}</a>' for t in p["themes"])
    apa = citation_apa(p)
    bib = bibtex(p)
    head_title = f"{p['title']} — Labib Shami"
    header_n = nested(header).replace(' aria-current="page"', "")
    header_n = header_n.replace('href="../../research.html"', 'href="../../research.html" aria-current="page"', 1)
    footer_n = nested(footer)
    short = p["title"] if len(p["title"]) < 60 else p["title"][:57].rsplit(" ", 1)[0] + "…"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(head_title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="Labib Shami">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:site_name" content="Labib Shami">
{chr(10).join(meta)}
<link rel="icon" href="../../img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="../../fonts/newsreader-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../../css/site.css">
<script>document.documentElement.classList.add('js')</script>
<script src="../../js/site.js" defer></script>
<script type="application/ld+json">{ld_json}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{header_n.strip()}
<main id="main">
  <article>
    <header class="paper-head">
      <div class="wrap">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="../../index.html">Home</a></li>
            <li><a href="../../research.html">Research</a></li>
            <li><a href="../../research.html#publications">Publications</a></li>
            <li aria-current="page">{e(short)}</li>
          </ol>
        </nav>
        <p class="eyebrow">{e(TYPE_LABEL[p['type']])} · {p['year']}</p>
        <h1>{e(p['title'])}</h1>
        <p class="paper-authors">{authors_html(p['authors'])}</p>
        <p class="paper-venue"><span class="venue">{e(p['venue'])}</span>{venue_bits(p)} {badges(p)}</p>
        <div class="btn-row">
          {' '.join(buttons)}
        </div>
      </div>
    </header>
    <div class="wrap paper-layout">
      <div class="prose">
        <h2>Summary</h2>
        <p class="lede">{e(p['summary'])}</p>
        <p class="note">This summary was written for this website from the published abstract. The publisher’s abstract and full text are the authoritative versions. No full text is reproduced here.</p>
        <h2>Research theme</h2>
        <p class="chips">{theme_links}</p>
        <h2>Related publications</h2>
        <ul>
{rel_html}
        </ul>
{('        <h2>Related policy analysis</h2>' + chr(10) + '        <ul>' + chr(10) + pol_html + chr(10) + '        </ul>') if pol_html else ''}
        <p><a class="arrow-link" href="../../research.html#publications">All publications</a></p>
      </div>
      <aside class="paper-aside" aria-label="Publication details and citation">
        <section class="panel" aria-labelledby="details-h">
          <h2 id="details-h">Details</h2>
          <dl>
{dl_html}
          </dl>
        </section>
        <section class="panel" aria-labelledby="cite-h">
          <h2 id="cite-h">Cite</h2>
          <p class="cite-box" id="cite-apa">{e(apa)}</p>
          <button type="button" class="btn btn--ghost btn--small copy-btn" data-copy-target="cite-apa">Copy citation</button>
          <details>
            <summary>BibTeX</summary>
            <pre class="bibtex" id="cite-bib">{e(bib)}</pre>
            <button type="button" class="btn btn--ghost btn--small copy-btn" data-copy-target="cite-bib">Copy BibTeX</button>
          </details>
        </section>
      </aside>
    </div>
  </article>
</main>
{footer_n.strip()}
</body>
</html>
"""


# ---------------------------------------------------------------- checks
def check(pubs, policy, media) -> list[str]:
    issues = []
    seen = set()
    for p in pubs:
        for k in ("id", "slug", "title", "authors", "year", "venue", "type", "status", "themes", "summary"):
            if not p.get(k):
                issues.append(f"{p.get('id')}: missing {k}")
        if p["slug"] in seen:
            issues.append(f"duplicate slug {p['slug']}")
        seen.add(p["slug"])
        if p.get("doi") and not re.match(r"^10\.\d{4,9}/\S+$", p["doi"]):
            issues.append(f"{p['id']}: bad DOI {p['doi']}")
        if ME not in p["authors"]:
            issues.append(f"{p['id']}: {ME} not in authors")
        if p["type"] not in TYPE_LABEL or p["status"] not in STATUS_LABEL:
            issues.append(f"{p['id']}: bad type/status")
    dois = [p["doi"].lower() for p in pubs if p.get("doi")]
    if len(dois) != len(set(dois)):
        issues.append("duplicate DOI")
    for r in policy["reports"]:
        if not r["url"].startswith("https://"):
            issues.append(f"{r['id']}: bad url")
    for m in media["items"]:
        if not m["url"].startswith("https://"):
            issues.append(f"{m['id']}: bad url")
        if m["kind"] not in media["kinds"]:
            issues.append(f"{m['id']}: unknown kind")
    return issues


def replace_region(path: Path, name: str, content: str) -> None:
    page = path.read_text(encoding="utf-8")
    pat = re.compile(rf"(<!-- {name}:START -->)(.*?)(<!-- {name}:END -->)", re.S)
    if not pat.search(page):
        raise SystemExit(f"{path.name}: markers for {name} not found")
    page = pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(3), page)
    path.write_text(page, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate data only")
    ap.add_argument("--base", help="absolute production URL, e.g. https://example.org/ (writes sitemap.xml)")
    a = ap.parse_args()

    pdata, policy, media = load("publications.json"), load("policy.json"), load("media.json")
    pubs, themes = pdata["publications"], pdata["themes"]
    issues = check(pubs, policy, media)
    if issues:
        print("Data problems:\n  " + "\n  ".join(issues))
        return 1
    print(f"OK: {len(pubs)} publications, {len(policy['reports'])} reports, {len(media['items'])} media items")
    if a.check:
        return 0

    replace_region(SITE / "research.html", "BIB", render_bibliography(pubs, themes))
    replace_region(SITE / "policy.html", "POLICY", render_policy(policy))
    replace_region(SITE / "media.html", "MEDIA", render_media(media))

    research = (SITE / "research.html").read_text(encoding="utf-8")
    header, footer = extract(research, "HEADER"), extract(research, "FOOTER")
    for p in pubs:
        d = SITE / "publications" / p["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(paper_page(p, pubs, themes, policy, header, footer), encoding="utf-8")
    (DATA / "publications.bib").write_text(
        f"% Labib Shami — publications (generated {_dt.date.today().isoformat()} from data/publications.json)\n\n"
        + "\n\n".join(bibtex(p) for p in pubs) + "\n", encoding="utf-8")
    print(f"Wrote {len(pubs)} paper pages and data/publications.bib")

    if a.base:
        base = a.base if a.base.endswith("/") else a.base + "/"
        urls = ["", "research.html", "policy.html", "media.html", "teaching.html", "about.html"] + [p["page_url"] for p in pubs]
        today = _dt.date.today().isoformat()
        xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        xml += [f"  <url><loc>{e(base + u)}</loc><lastmod>{today}</lastmod></url>" for u in urls]
        xml.append("</urlset>")
        (SITE / "sitemap.xml").write_text("\n".join(xml) + "\n", encoding="utf-8")
        robots = (SITE / "robots.txt").read_text(encoding="utf-8")
        robots = re.sub(r"(?m)^Sitemap:.*\n?", "", robots).rstrip() + f"\nSitemap: {base}sitemap.xml\n"
        (SITE / "robots.txt").write_text(robots, encoding="utf-8")
        print(f"Wrote sitemap.xml for {base}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
