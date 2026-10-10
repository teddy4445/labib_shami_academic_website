#!/usr/bin/env python3
"""Basic zero-dependency audit of a deployable HTML/CSS/JS static website.

Usage: python3 audit_static_site.py /path/to/site
Checks local links/files/fragments, common accessibility/SEO structural basics,
JSON validity and obvious Node build artifacts. Does not replace browser/WCAG QA.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SKIP_DIRS = {".git", ".claude", "node_modules", "__pycache__"}
HTML_EXT = {".html", ".htm"}
EXTERNAL_SCHEMES = {"https", "http", "mailto", "tel", "sms", "data", "blob"}
NODE_FILES = {"package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "vite.config.js", "vite.config.ts"}


@dataclass
class Link:
    tag: str
    attr: str
    value: str
    line: int


class HtmlAudit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[Link] = []
        self.ids: list[str] = []
        self.images_without_alt: list[int] = []
        self.iframes_without_title: list[int] = []
        self.blank_rel_issues: list[int] = []
        self.missing_hrefs: list[int] = []
        self.h1_count = 0
        self.main_count = 0
        self.language = ""
        self.title_parts: list[str] = []
        self.in_title = False
        self.description = ""
        self.robots = ""
        self.viewport = False
        self.charset = False
        self.has_doctype = False

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype html"):
            self.has_doctype = True

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        at = dict(attrs)
        line = self.getpos()[0]
        if tag == "html":
            self.language = (at.get("lang") or "").strip()
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.main_count += 1
        if tag == "title":
            self.in_title = True
        if tag == "meta":
            if (at.get("name") or "").lower() == "description":
                self.description = at.get("content") or ""
            if (at.get("name") or "").lower() == "robots":
                self.robots = at.get("content") or ""
            if (at.get("name") or "").lower() == "viewport":
                self.viewport = bool(at.get("content"))
            if "charset" in at:
                self.charset = True
        if tag == "img" and "alt" not in at:
            self.images_without_alt.append(line)
        if tag == "iframe" and not (at.get("title") or "").strip():
            self.iframes_without_title.append(line)
        if tag == "a":
            if not (at.get("href") or "").strip():
                self.missing_hrefs.append(line)
            if (at.get("target") or "").lower() == "_blank":
                rel = set((at.get("rel") or "").lower().split())
                if not {"noopener", "noreferrer"}.intersection(rel):
                    self.blank_rel_issues.append(line)
        id_ = at.get("id")
        if id_:
            self.ids.append(id_)
        for attr in ("href", "src", "poster"):
            if attr in at and at[attr] is not None:
                self.links.append(Link(tag, attr, at[attr], line))
        if at.get("srcset"):
            for spec in at["srcset"].split(","):
                value = spec.strip().split()[0] if spec.strip() else ""
                if value:
                    self.links.append(Link(tag, "srcset", value, line))

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False


def local_target(site: Path, source: Path, value: str):
    val = value.strip()
    if not val:
        return None
    if val.startswith("//"):
        return None  # External protocol-relative URL (avoid using for critical assets)
    parsed = urlsplit(val)
    if parsed.scheme:
        return None
    if not parsed.path and not parsed.fragment:
        return None
    root_absolute = parsed.path.startswith("/")
    relative_path = unquote(parsed.path)
    if root_absolute:
        dest = site / relative_path.lstrip("/")
    elif relative_path:
        dest = source.parent / relative_path
    else:
        dest = source
    if relative_path.endswith("/") or dest.is_dir():
        dest = dest / "index.html"
    return dest.resolve(), unquote(parsed.fragment), root_absolute


def visible_path(path: Path, root: Path):
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def audit(site: Path):
    errors: list[str] = []
    warnings: list[str] = []
    html: dict[Path, HtmlAudit] = {}
    if not (site / "index.html").is_file():
        errors.append("Missing root index.html")
    for forbidden in NODE_FILES:
        if (site / forbidden).exists():
            warnings.append(f"Build/dependency artifact in deployed root (review against no-build requirement): {forbidden}")
    if not (site / ".nojekyll").exists():
        warnings.append("No .nojekyll file: add when deploying this repository to GitHub Pages")
    if (site / "robots.txt").is_file() and re.search(r"(?im)^\s*Disallow:\s*/\s*$", (site / "robots.txt").read_text(encoding="utf-8")):
        warnings.append("robots.txt contains Disallow: / - remove this site-wide exclusion before production release")
    if not (site / "robots.txt").exists():
        warnings.append("No robots.txt: recommended for a production public website")
    if not (site / "sitemap.xml").exists():
        warnings.append("No sitemap.xml: create once canonical production origin is known")

    for file in sorted(site.rglob("*")):
        if any(part in SKIP_DIRS or part.startswith(".") and part not in {".nojekyll"} for part in file.relative_to(site).parts):
            continue
        if not file.is_file():
            continue
        name = visible_path(file, site)
        if file.suffix.lower() == ".json":
            try:
                json.loads(file.read_text(encoding="utf-8-sig"))
            except (UnicodeError, json.JSONDecodeError) as exc:
                errors.append(f"{name}: invalid JSON: {exc}")
        if file.suffix.lower() not in HTML_EXT:
            continue
        parser = HtmlAudit()
        try:
            raw = file.read_text(encoding="utf-8-sig")
            parser.feed(raw)
            parser.close()
        except Exception as exc:
            errors.append(f"{name}: could not parse HTML: {exc}")
            continue
        html[file.resolve()] = parser
        if not parser.has_doctype:
            warnings.append(f"{name}: missing <!doctype html>")
        if not parser.language:
            errors.append(f"{name}: <html> missing lang attribute")
        if not "".join(parser.title_parts).strip():
            errors.append(f"{name}: missing/noninformative <title>")
        if "noindex" in parser.robots.lower():
            warnings.append(f"{name}: robots noindex set; remove before intended public launch")
        if not parser.description.strip():
            warnings.append(f"{name}: missing page meta description")
        if not parser.viewport:
            warnings.append(f"{name}: missing viewport meta tag")
        if not parser.charset:
            warnings.append(f"{name}: missing charset declaration")
        if parser.h1_count != 1:
            warnings.append(f"{name}: expected one <h1>, got {parser.h1_count}")
        if parser.main_count != 1:
            warnings.append(f"{name}: expected one <main>, got {parser.main_count}")
        for duplicate, count in Counter(parser.ids).items():
            if count > 1:
                errors.append(f"{name}: duplicate id='{duplicate}' ({count} times)")
        for line in parser.images_without_alt:
            errors.append(f"{name}:{line}: img missing alt (use alt=\"\" if decorative)")
        for line in parser.iframes_without_title:
            warnings.append(f"{name}:{line}: iframe missing title")
        for line in parser.blank_rel_issues:
            warnings.append(f"{name}:{line}: target=_blank link lacks rel=noopener/noreferrer")
        for line in parser.missing_hrefs:
            warnings.append(f"{name}:{line}: anchor lacks useful href")
        if re.search(r"<!--\s*TODO\b|\[TODO\]|\bYOUR[-_ ]NAME\b", raw, re.I):
            warnings.append(f"{name}: appears to contain authoring placeholder/TODO")

    for file, parser in html.items():
        name = visible_path(file, site)
        for item in parser.links:
            value = item.value.strip()
            if re.match(r"(?i)^\s*(javascript|vbscript):", value):
                errors.append(f"{name}:{item.line}: unsafe URL scheme in {item.attr}")
                continue
            if item.attr == "href" and item.tag == "a" and value == "#":
                warnings.append(f"{name}:{item.line}: fake anchor href='#'")
                continue
            result = local_target(site, file, value)
            if result is None:
                continue
            target, fragment, is_root_absolute = result
            if is_root_absolute:
                warnings.append(f"{name}:{item.line}: root-absolute URL {value!r} may fail on GitHub Pages project subpath")
            if not target.is_relative_to(site):
                errors.append(f"{name}:{item.line}: link escapes site root: {value}")
                continue
            if not target.is_file():
                errors.append(f"{name}:{item.line}: broken local {item.tag}.{item.attr}={value!r}")
                continue
            if fragment and target.suffix.lower() in HTML_EXT:
                linked = html.get(target)
                if linked and fragment not in linked.ids:
                    warnings.append(f"{name}:{item.line}: fragment #{fragment} not found in {visible_path(target, site)}")
    return html, errors, warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("site", type=Path, help="Root containing index.html")
    args = ap.parse_args()
    site = args.site.resolve()
    if not site.is_dir():
        ap.error("Given path is not a directory")
    html, errors, warnings = audit(site)
    print(f"Static site audit: {site} | {len(html)} HTML pages | {len(errors)} errors | {len(warnings)} warnings")
    for entry in errors:
        print("ERROR:", entry)
    for entry in warnings:
        print("WARN: ", entry)
    if not errors:
        print("No structural errors detected. Still check content accuracy, WCAG, responsive layout and browser behavior manually.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
