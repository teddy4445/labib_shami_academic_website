# Labib Shami — research & website-content pack

**Research performed:** 2026-10-10  
**Person:** Dr. Labib Shami (לביב שאמי / لبيب شامي), economist in Israel.  
**Purpose:** Hand this directory to Claude Code with the previously prepared *academic website* skill kit to generate an accurate personal academic website.  
**Nature:** Original metadata, curated links, drafts, and evidence notes. **Not** a mirror of third-party content.

## What is inside

| Folder | Contents |
|---|---|
| `profile/` | Verified public professional facts, draft bios, unresolved questions |
| `publications/` | 28 curated scholarly records (JSON/CSV/draft BibTeX), featured paper concepts |
| `policy/` | 13 Taub Center research reports with official landing-page links |
| `media/` | 13 videos, podcasts, radio, opinion and press references |
| `assets/` | Portrait sources, image permission checks and asset request list |
| `sources/` | 69 provenance URLs and source-confidence labels |
| `papers/` | PDF access list; information on acceptable paper-to-HTML processing |
| `RESEARCH_INDEX.html` | Offline browseable, clickable source index (no build needed) |
| `brief/` | Site plan, homepage messaging and content priorities |
| `prompts/` | One master prompt for Claude Code |
| `tools/` | Local data validator; Python standard library only |

## Important boundaries

- **NO publication full-text PDFs are embedded.** Third-party publishers and institutional publishers may restrict redistribution. Paper DOIs and official report landing pages are supplied. An old public 2021 CV is provided as a link, not included as a binary.
- **NO third-party portrait or article images are embedded.** The asset manifest identifies sources and permissions to request.
- Items are *curated leads*, not an exhaustive, perfectly normalized Scopus or Crossref export. The University of Haifa currently lists **36 research outputs**; ResearchGate lists **37 records**, including duplicates and preprints. Our 28 items are deduplicated draft scholarly works, separate from 13 Taub reports.
- A few statuses, journal years, full coauthor lists, and book years require review. Blank authors are deliberately not guessed.
- Full-text conversion requires permitted PDF access, citation preservation, human review of formulas/tables/figures, and a clear version/licensing statement.
- Public pages should contain **no family/private details** found in some institutional bios.
- English-first recommendation; add Hebrew/Arabic with human-quality translation and RTL support after Labib confirms.

## Fastest route

1. Unzip this folder into your website development project under `materials/labib-shami-research-pack/`.
2. Install the `academic-website-claude-kit.zip` skills from the previous handoff in `.claude/skills/`.
3. Put any **approved** photos, complete CV, self-owned papers, slide decks and teaching materials in `materials/approved-assets/`.
4. Paste `prompts/CLAUDE_CODE_START.md` into Claude Code.
5. Run `python3 tools/validate_data.py` to check records before launch.

## Review order

`profile/APPROVAL_QUESTIONS.md` → `brief/WEBSITE_BLUEPRINT.md` → `publications/FEATURED_RESEARCH.md` → `media/media.csv` → `assets/asset_manifest.csv`.

See `sources/source_registry.csv` for every source reference. Dates are issue year or verified public appearance when known, not always first-online date.
