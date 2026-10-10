# Publication reconciliation (10 October 2026)

Source of truth for the site: `site/data/publications.json` (public). The full provenance version is `research/publications-master.json`, which adds sources, verification notes and summary basis.

## Sources compared

| Source | Records with Labib Shami | Notes |
|---|---|---|
| Research pack `publications/publications.json` | 28 | Curated leads; 6 IJESB items had no authors; 3 items had no DOI |
| Crossref (author query + ORCID filter) | 30 DOIs | Includes **5 duplicate "early" Inderscience DOIs** (10.1504/IJESB.2024.100xxxxx) for IJESB papers |
| OpenAlex (author ORCID filter) | 35 works | Includes duplicate IJESB DOIs, 4 preprints, 2 Zenodo deposits of Taub reports |
| ORCID public works list | 24 groups | Includes arXiv version of the co-authorship paper |
| arXiv API | 4 preprints | 3 are earlier versions of published articles |
| University of Haifa CRIS | "37 research outputs" (36 articles, 1 report) | List page not readable (bot protection). The count likely includes the IJESB duplicates and Taub items. |

## Result: 28 distinct works

| Type | Count |
|---|---|
| Peer-reviewed journal articles | 25 (2 of them online first: `labib-003`, `labib-004`) |
| Book chapter (Springer handbook, living reference) | 1 (`labib-026`) |
| Preprints / working papers with no journal version found | 2 (`labib-005` SSRN, `labib-009` arXiv) |

## De-duplication decisions

| Duplicate set | Kept | Linked as version / dropped |
|---|---|---|
| *Cooperative Game-Theoretic Framework for Sustainable UN Financing* (Economies 2026) vs arXiv 2602.15062 *Cooperative Game Theory Model for Sustainable UN Financing…* | Journal article | arXiv linked as "Earlier preprint" |
| *Academic co-authorship is a risky game* (Scientometrics 2023) vs arXiv 2207.13170 | Journal article | arXiv linked |
| *Economical–epidemiological analysis of the coffee trees rust pandemic* (Chaos 2024) vs arXiv 2304.14515 | Journal article | arXiv linked |
| IJESB 2024 papers: 5 of 6 articles have two DOIs each (early `…100xxxxx` and final) with **different author orders** | Final DOI, with author order from the Inderscience landing page (`dc.Creator` metadata), checked for all 6 | Early DOIs dropped. Flagged for Dr. Shami to confirm. |
| *Dynamic monetary equilibrium…* (J. Macroeconomics): 2018 online, 2019 issue; the 2021 CV lists it twice | One record, dated 2019 (vol. 62) | — |
| *Pandemic management by a spatio–temporal mathematical model*: 2021 online, 2023 issue | One record, dated 2023 | — |
| DSABNS 2021 conference abstract (listed on the ACML lab site) | Not listed | A conference abstract of the IJNSNS model, not a separate paper |
| Zenodo deposits of two Taub reports | Not listed as scholarly works | Reports are on the Policy page instead |

## Corrections and additions relative to the research pack

| Pack ID | Change |
|---|---|
| labib-001 | Added CC BY 4.0 licence and arXiv preprint link; date 7 July 2026 |
| labib-002 | Volume/issue/pages 33(2) 159–177 |
| labib-003 | Venue full name *Innovation: Organization & Management*; online first 19 Apr 2026 |
| labib-004 | Online first 19 Feb 2026; CC BY 4.0 |
| labib-005 | DOI found: **10.2139/ssrn.6022246** (SSRN, posted 5 Jan 2026); replaces the ResearchGate placeholder URL |
| labib-006 | 15(4) 1021–1044 (issue Dec 2025; online 20 Apr 2025). Presented at GLO-Berlin-2024 |
| labib-007 | 26(2) 288–303; online 5 Oct 2024, issue June 2025 |
| labib-008 | 51(3) 524–546; online 10 Jul 2024 |
| labib-010 | 34(11) 113112; CC BY-NC 4.0; arXiv 2304.14515 linked |
| labib-011 to 016 | **Full author lists added** (6 authors each: Gil Cohen, Limor Yehuda, Sagit Barel-Shaked, Labib Shami, Arie Herscovici/Hershkovici, Osnat Akirav, in a different order per paper), plus volume/issue/pages |
| labib-019 | 128(12) 6495–6507; CC BY 4.0; arXiv linked |
| labib-020 | DOI case normalised (10.34768/amcs-2023-0042); 33(4); open access |
| labib-022 | **DOI found: 10.1016/j.seps.2023.101553** (vol. 87, 101553). Replaces the ResearchGate placeholder. |
| labib-023 | 24(6) 2307–2324 (2023); online 2021 |
| labib-025 | 35(1) 1833–1861 (2022); CC BY 4.0 |
| labib-026 | **DOI found: 10.1007/978-3-319-57365-6_227-1**; online 29 Oct 2021; ed. Klaus F. Zimmermann; pp. 1–24 |
| labib-027 | 61, 101820 (Jan 2020) |
| labib-028 | 62, 103018 (Dec 2019) |

## Themes (filters on the Research page)

`money-credit` (3) · `non-observed` (7) · `smes-local` (8) · `crisis` (8) · `political-economy` (5). Some works carry two themes. Themes are editorial groupings. Dr. Shami may want to rename or regroup them.

## Summaries

Each work has a 1–3 sentence summary in plain English, written for the site. Basis:

- Publisher or repository abstract read via Crossref/OpenAlex/Semantic Scholar/arXiv/SSRN/publisher page: 25 works.
- Abstract as published in the co-author lab website data (ACML `academic-publications.json`), because ScienceDirect was not readable: `labib-021`, `labib-022`, `labib-024`.

No numerical results were added to a summary unless they appear in the abstract (for example, the 513 and 766 survey samples). All summaries need author review before launch (`NEEDS_LABIB_APPROVAL.md`).
