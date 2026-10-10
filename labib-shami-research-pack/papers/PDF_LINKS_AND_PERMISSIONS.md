# How to obtain papers and prepare web editions

## Verified public source pages

- Taub center institutional CV (historical 2021): https://www.wgalil.ac.il/wp-content/uploads/2021/12/Shami_Labib_2021.pdf
- Taub Center State of the Nation Report 2019 PDF: https://www.taubcenter.org.il/wp-content/uploads/2020/12/snr2019english.pdf (includes Household Debt in Israel)
- Taub Center State of the Nation Report 2023 PDF: https://www.taubcenter.org.il/wp-content/uploads/2024/03/SNR-ENG-2023-online.pdf (includes Interest, Inflation and Mortgages)
- 2026 Economies article: https://www.mdpi.com/2227-7099/14/7/263 (publisher full text, inspect license)
- Sweden informal economy article: https://link.springer.com/article/10.1007/s10614-025-11276-6 (publisher version, open access listed, verify license)
- Academic co-authorship article: https://link.springer.com/article/10.1007/s11192-023-04843-x (publisher page)
- Preprint on tax evasion AI modeling: https://arxiv.org/abs/2501.18177 (arXiv provides a PDF; verify version terms)

## Rules for developer

1. Link out to publisher full text and DOI by default. A public download page is NOT permission to mirror the binary in another site.
2. Before copying a PDF into `site/`, check exact article license or use the author's own manuscript with permission. Record the license, source, version, credit, and URL in `site/data/papers.json`.
3. For PDF-to-HTML, use a temporary offline extraction pass (Python permitted for content-preparation only), validate Unicode, math, citations, references, captions, figure placement, heading order and accessibility. Never publish a raw uncorrected conversion.
4. Do not copy publisher typesetting or figures except under a license that permits reuse. Redraw charts from appropriately licensed underlying data or secure permission.
5. Keep original private files outside `site/` until content and licenses are cleared.
6. Every paper card should have title, authors (if verified), year, journal, DOI, link, and a clear “preprint” vs “peer-reviewed” status.

## Automated retrieval policy

No binary PDFs were downloaded into this research pack. Claude Code may download from verified, permissively licensed sources on its own working machine after checking the license. No proxy scraping, bypassing paywalls, or circumventing publisher restrictions.

### Additional verified direct links
- Mixed-city migration 2023 report: https://www.taubcenter.org.il/wp-content/uploads/2023/05/Migration-Patterns-ENG-2023-1.pdf
- Supervised daycare 2021 report: https://www.taubcenter.org.il/wp-content/uploads/2021/11/EnrollmentinSupervisedDaycareEng-1.pdf
