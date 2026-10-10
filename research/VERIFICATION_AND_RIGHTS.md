# Verification and rights

**Subject:** Dr. Labib Shami (לביב שאמי · لبيب شامي), economist, ORCID [0000-0002-3127-5109](https://orcid.org/0000-0002-3127-5109)
**Research date:** 10 October 2026 (all access dates below are this date unless stated)
**Scope:** everything that appears on the public pages in `site/`. Detailed claim-by-claim evidence is in `research-evidence.csv`. The list of open questions is in `claims-needing-review.md`, summarised in `../NEEDS_LABIB_APPROVAL.md`.

This folder is private authoring material. Do **not** copy `research/` (or `labib-shami-research-pack/`, `materials/`) into the deployed website.

---

## 1. How verification was done

| Step | Method | Result |
|---|---|---|
| Local pack audit | Read all 26 files of `labib-shami-research-pack/` plus the kit instructions | Used as leads, not as proof. Every public claim was re-checked online (§2). |
| Identity | Matched ≥2 independent anchors (§3) | Single person confirmed. Namesakes excluded. |
| Institutional roles | Taub Center EN + HE profiles, Western Galilee College (WGC) official faculty lists, University of Haifa research portal (CRIS), WGC SMB25 conference page, RIC profile | Taub role verified. WGC teaching roles verified, but **rank not stated** by WGC. Haifa listed as **former affiliation**. |
| Bibliography | Crossref REST API (author query + ORCID filter), OpenAlex (ORCID filter), ORCID public API works list, arXiv API, publisher landing pages (Inderscience, Springer, MDPI), SSRN | 28 works reconciled: 25 journal articles, 1 chapter, 2 preprints/working papers. Details in `publication-reconciliation.md`. |
| Policy reports | Each Taub Center research page opened; titles, dates, authors and PDF links recorded | All 13 reports confirmed as Shami-authored or co-authored. Corrections in `policy-media-verification.md`. |
| Media | Each item opened; original-language titles taken from the page; YouTube titles and upload dates from YouTube pages/oEmbed | 18 items published; 1 excluded as unconfirmed. |
| Tools | WebFetch/WebSearch (research subagents); the in-app browser on the user's desktop for Crossref/OpenAlex/ORCID/arXiv JSON and for pages that block automated fetchers | See §6 for sources that could not be read. |

Draft CV of July 2021 (hosted by WGC) was used **only for historical facts** (degrees, thesis, supervisors). It was not used for any present-tense claim.

## 2. Status of the facts shown on the site

| Public statement | Status | Primary source(s) |
|---|---|---|
| Senior Researcher, Taub Center for Social Policy Studies in Israel | Verified (current) | Taub EN/HE profiles |
| Faculty member, Department of Economics, WGC; lecturer in Economics, Management and the MA in Economics & Management; student advisor in Management; listed on English-taught BA faculty | Verified (current wording on official WGC pages) | wgalil.ac.il faculty lists (School of Management; BA Economics; international BA) |
| Academic rank at WGC | **Not shown.** "Senior lecturer" appears only in a 2025 conference bio; the 2021 CV says "Lecturer"; official pages show no ranks | needs Dr. Shami |
| Taught at University of Haifa as Teaching Associate | Verified as **past** ("Former affiliation", Haifa CRIS, 2019–2026). Shown in past tense | cris.haifa.ac.il |
| PhD Economics, University of Haifa, 2018; thesis title; supervisors Anna Rubinchik and Nissim Cohen | Verified (historical; Taub profile confirms the Haifa doctorate) | 2021 CV; Taub profile |
| Graduate studies in Economics, University of Haifa & Technion, 2015; first degree, Open University, 2011 | Historical, single source | 2021 CV |
| Co-author with Prof. Benjamin Bental of the State of the Nation Report macro chapter, 2021–2025 | Verified | Taub research pages for each year |
| Two Hebrew guidebooks, "יסודות הכלכלה" and "מבוא לסטטיסטיקה" | Titles verified. **Years and publisher conflict between sources, so they are not shown.** | Taub HE/EN profiles; SMB25 bio; 2021 CV |
| UC San Diego guest lecture (ECON 168, The Israeli Economy) | Verified (two sources) | Taub news item 10.03.2023; Yuval Heller's UCSD teaching page |
| GLO-Berlin-2024 presentation, 20 April 2024 | Verified | glabor.org programme |
| SMB 2025 scientific committee (WGC) | Verified | events.wgalil.ac.il/SMB25 |
| Contact email labibs@taubcenter.org.il | Published by the Taub Center as his professional address. **Shown pending his confirmation.** | Taub profile |
| Name in Hebrew and Arabic | Verified | Taub HE profile; Radio Ashams page title |
| GLO Fellow | **Not shown.** Self-reported in a 2025 bio only; not confirmable on glabor.org | — |

Publication counts on the site ("25 peer-reviewed journal articles, one handbook chapter and two working papers") describe **this site's reconciled list** and are not a claim about completeness. No citation counts, h-index, rankings or awards appear anywhere.

## 3. Identity resolution (summary)

Anchors that all point to the same person: (1) ORCID 0000-0002-3127-5109 lists employment at the University of Haifa (Economics) and Western Galilee College; (2) the same ORCID is attached to his Crossref/PubMed records (e.g. *Chaos* 2024, *Economies* 2026, *Journal of Banking Regulation* 2025); (3) Taub, WGC, Haifa and RIC profiles share name, field and affiliations; (4) recurring co-authors (Bental at Taub; Lazebnik, Rachevski, Bunimovich-Mendrazitsky); (5) the doctoral thesis title matches his sole-authored *Journal of Macroeconomics* article. Similar names that were excluded are listed in `identity-resolution.md`.

## 4. Rights and licensing

### 4.1 What the deployed site contains

| Asset | Origin | Rights basis |
|---|---|---|
| All page text, summaries, glosses, biographies | Written for this site from verified sources | Original wording. Paper summaries paraphrase published abstracts and are not copies. They are labelled on every paper page. |
| Bibliographic metadata (titles, authors, venues, DOIs) | Crossref/publisher records | Facts; citation use |
| Diagram, pillar glyphs, logo mark, favicon, book-spine graphics | Drawn for this site as inline SVG/CSS | Original |
| Fonts: Newsreader, Source Sans 3 (`site/fonts/`) | Fontsource packages (npm registry) | SIL Open Font License 1.1. Licence files shipped in `site/fonts/`. |
| `site/data/*.json`, `publications.bib` | Generated from verified metadata | Original compilation |

### 4.2 What the site deliberately does NOT contain

| Not included | Why | What is shown instead |
|---|---|---|
| Portraits (Taub Center photo, ResearchGate avatar) | No reuse permission. Website access is not a licence. | Portrait-independent hero with an original conceptual diagram |
| Publisher PDFs or full texts | Copyright and licences vary. No author manuscripts were supplied. | DOI and publisher links; arXiv/SSRN links where a free version exists |
| Taub Center report PDFs, figures and charts | No redistribution permission | Links to the Taub Center's official pages and PDFs |
| Publisher abstracts verbatim | Copyright | Original summaries |
| YouTube thumbnails, press images, logos | No permission | Click-to-load video facade with original styling. No institutional logos. |
| The 2021 CV | Historical, possibly outdated; no permission to mirror | Facts used with attribution in research files only |
| Family or personal details present in some institutional bios | Privacy | Omitted entirely |

### 4.3 Open-access works (licence verified from Crossref licence metadata)

| Work | Licence | Could be converted to full-text HTML later? |
|---|---|---|
| Shami & Lazebnik (2026), *Economies* 14(7) 263 | CC BY 4.0 | Yes, with attribution, after a careful fidelity review |
| Lazebnik, Shami & Peretz-Andersson (2026), *Computational Economics* | CC BY 4.0 | Yes (same conditions) |
| Lazebnik, Beck & Shami (2023), *Scientometrics* 128(12) | CC BY 4.0 | Yes (same conditions) |
| Lazebnik, Shami & Bunimovich-Mendrazitsky (2022), *Economic Research-Ekonomska Istraživanja* 35(1) | CC BY 4.0 | Yes (same conditions) |
| Lazebnik, Rosenfeld & Shami (2024), *Chaos* 34(11) | CC BY-NC 4.0 | Yes for non-commercial use, with attribution |
| Lazebnik, Shami & Bunimovich-Mendrazitsky (2023), *AMCS* 33(4) | Open access; licence not in Crossref | Check the journal licence first |
| arXiv 2501.18177, 2602.15062, 2207.13170, 2304.14515; SSRN 6022246 | Repository licences not checked | Link only |

No PDF-to-HTML conversion was performed. The optional `pdf_to_draft_html.py` helper from the kit was **not** run, because no permitted source files were supplied and an unreviewed conversion must not be published.

### 4.4 Third-party embeds and privacy

- YouTube videos (Taub Center channel and two third-party channels) appear behind a click-to-load facade. Nothing is requested from YouTube until a visitor presses play, and the player then loads from `youtube-nocookie.com`. All four videos returned embeddable oEmbed responses on 10 October 2026.
- Radio Ashams, Globes, Bizportal, Bokra, ynet, The Jerusalem Post and others are **linked only**. Their audio, text and images are not embedded.
- The site loads no analytics, trackers, external fonts or CDNs. Automated QA confirmed zero third-party requests on page load (`qa-report.md`).

## 5. Media title policy

Titles are reproduced exactly as published in their original language and script (Arabic, Hebrew or English), with `lang` and `dir` attributes. English glosses are short translations written for this site and are labelled "English gloss". They are not official translations. Where a page title and the YouTube title differ slightly (e.g. en dash vs hyphen), the YouTube title is used for videos.

## 6. Sources that could not be read (documented, not worked around)

| Source | Problem | Effect |
|---|---|---|
| University of Haifa CRIS outputs list (37 items) | Bot-protection page (automated fetch and in-app browser) | Our list was reconciled via Crossref/OpenAlex/ORCID. CRIS count not reconciled item by item. |
| WGC personal staff page (`wgalil.ac.il/academicstaff/2453`) | robots-disallowed | Rank unverified; department lists used instead |
| ScienceDirect landing pages (Elsevier) | Bot check | Summaries for 3 Elsevier articles rely on abstracts published on the co-author lab's website data (ACML) and Semantic Scholar |
| osimhistoria.com (Osim Heshbon podcast, 2023) | robots-disallowed; episode page 404 in browser | **Excluded** from the site as unconfirmed |
| LinkedIn, Google Scholar | Login/robots | Not linked |
| Direct `curl` to Crossref, OpenAlex, ORCID, Taub, WGC | Sandbox egress policy (HTTP 403) | Same data read through the sanctioned web tools / in-app browser |
| Crossref via WebFetch | Rate-limited (HTTP 429) | Read via the in-app browser instead |

## 7. Re-verification checklist before launch or yearly

1. Re-open the Taub EN profile (title) and the WGC faculty list (roles).
2. Run a Crossref query for `query.author=Labib+Shami` and `filter=orcid:0000-0002-3127-5109`. Add new DOIs to `site/data/publications.json`, then run `python3 tools/site_tool.py`.
3. Update online-first items (`labib-003`, `labib-004`) when volume and issue are assigned.
4. Check that the arXiv tax-evasion preprint (`labib-009`) and the SSRN working paper (`labib-005`) have not been published. If one has, change its type and status and keep the preprint as a version.
5. Re-check that the video links still play and that the media URLs still resolve.
