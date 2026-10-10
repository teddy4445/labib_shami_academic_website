# Agent B notes: Taub policy reports and media (checked 2026-10-10)

The structured results are in `agentB_policy_media.json`.

## How the checks were done
- Every page was read with WebFetch. The proxy blocked curl to taubcenter.org.il and youtube.com, so I made no raw-HTML or PDF downloads, and no PDF author list was checked.
- Exact report days (dd.mm.yyyy) come from Taub listing pages: `/en/researches/economics-2/?date=YYYY`, `/en/tag-research/economy/` and `/en/tag-research/early-childhood/`. The report pages themselves show only month and year.
- I got YouTube titles and channels from oEmbed through WebFetch, and oEmbed worked for all four video IDs. The YouTube watch pages could not be read: one returned HTTP 429 and the others errored. I did not retry them, so no upload dates were verified.
- osimhistoria.com is robots-disallowed for WebFetch, so I could not open that page.

## Policy reports
- All 13 report pages exist and credit Labib Shami.
- **taub-011** (Coronavirus overview, 23.12.2020): authors are Benjamin Bental and Labib Shami.
- **taub-012** (Non-Observed Economy, 10.09.2020): Labib Shami is the sole author. A search-indexed PDF title calls it "Policy Paper No. 05.2020". That label comes from the search result, not from the page.
- **taub-010** (Daycare, 23.11.2021):
  - English page author list: Shavit Ben-Porat, John Gal, Labib Shami, Avner Elizur. Elizur has no role on the page.
  - Hebrew page author list: שביט בן-פורת, ג’וני גל, לביב שאמי, אלון סלע (research assistant).
  - Ben-Porat and Madhala are the same person: the photo alt text and bio slug on the English page use "Madhala".
  - "Avner Elizur" looks like an English-page error for Alon Sela, who appears as "Elon Seela" in the input's PDF note.
  - The PDF order the input claims was not verified.
- **Title corrections:**
  - taub-008 should read "Macroeconomic Trends in Israel: An Overview" and taub-009 "Macroeconomic Trends: An Overview". Neither has a year suffix.
  - taub-004 uses a typographic apostrophe (’).
- **Series:**
  - Only taub-003 (SNR 2025 chapter) and taub-004 (SNR 2024, chapter 1 of 8) show the series on the page.
  - The State of the Nation (SNR) index pages add more:
    - Book chapters: taub-005 (SNR 2023), taub-008 (SNR 2022), taub-009 (SNR 2021).
    - Executive summaries: taub-006 (SNR 2023) and taub-010 (SNR 2021).
    - taub-011 is probably the SNR 2020 macro chapter, but this is not confirmed.
- **Profile check:**
  - The English and Hebrew Taub profiles list 10 reports. They omit taub-005, taub-006 and taub-007, although those pages credit him.
  - No report by Shami is missing from the 13.
  - "The October War and Its Impact…" (Dec 2023) is credited only to "Taub Center researchers", so it is excluded.

## Media
- **Confirmed (10 of 13):** 001, 002, 003, 004, 005, 007, 009, 010, 011, 012 and 013.
- **media-007 resolved:** the YouTube title is «ד"ר לביב שאמי: חייבים לבדוק גם התנהלות עתידית של השוק לפני שלוקחים משכנתא», on Dr. Michael Mero's channel. The date is unknown.
- **media-005:** Yedioth Ahronoth via ynet, by Israel Volman. The metadata timestamp is 2025-02-16T22:00Z, which is 17 Feb 2025 in Israel. Shami is named together with co-researcher Dr. Teddy Lazebnik of Ariel University.
- **media-009:** confirmed by the Taub news item dated 10.03.2023 and by Yuval Heller's UCSD ECON 168 page, which calls him "Prof." Use the news-item URL instead of the category page.
- **media-013:** the Hebrew page embeds YouTube ID L1NVBmx2Xd0, which is a different video from media-012's mXoxr-9Xej4.
- **media-012:** the Taub page date is 02.02.2020. I could not verify the input date of 2020-01-19.
- **media-002:** this was a programme interview with an audio clip, not "reported commentary".
- **Unconfirmed:**
  - media-006: the title is «מהגרי פנים» and the video can be embedded, but Shami is not named in the metadata I could read.
  - media-008: the episode exists, dated 25/06/2023 and also at osimhistoria.com/osim-heshbon/ep88-mortgage_mistake, but I could not confirm that Shami is the guest.

## Additional media, 2025–2026
| Date | Outlet | How Shami appears | Report |
|---|---|---|---|
| 2026-09-16 | Bizportal | Named | CPI (taub-001) |
| 2026-05-11 | Bizportal | Quoted directly | Housing tenure (taub-002) |
| 2026-05-11 | Bokra (Arabic) | Indirect quote | Housing tenure (taub-002) |
| 2025-12-29 | Bizportal | Named | SNR 2025 (taub-003) |
| 2025-12-29 | Jerusalem Post | Named | SNR 2025 (taub-003) |

These articles did not name him: Kan (CPI, Sept 2026), JPost article 905563, and the Taub 2026 budget webinar.
