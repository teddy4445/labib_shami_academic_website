# Site plan

## Positioning (editorial interpretation; needs Dr. Shami's approval)

- **One sentence:** Labib Shami builds economic models of money, credit and the non-observed economy, and applies them to the policy questions households, businesses and governments face in Israel.
- **Hero statement:** "Studying the economy that official statistics record, *and the part they miss*." The line is drawn from his doctoral and continuing work on the non-observed economy, and suggests that the work is about measurement and evidence.
- **Not part of the brand:** consulting, unverified ranks or fellowships, citation metrics, personal or family details, first-person claims.

## Three pillars → evidence

| Pillar | Question | Evidence on the site |
|---|---|---|
| Money, credit & households | How do monetary policy and credit markets reach household budgets? | J. Macroeconomics 2019; EJPE 2020; J. Banking Regulation 2025; Taub: household debt 2019, mortgages 2023, CPI 2026 |
| The non-observed economy | How large is the economy official statistics miss, and what drives it? | Comp. Econ. 2024 (ML); Comp. Econ. 2026 (Sweden); IJESB 2024; Comp. Econ. 2024 (tax ABM); arXiv 2025; Taub 2020 |
| Policy, enterprise & resilience | Which public decisions help economies and businesses absorb shocks? | Local Gov. Studies 2025; SER 2026; Innovation 2026; JPM 2023; SEPS 2023; Economies 2026; EER 2025 |

## Audiences and actions

1. Academic researchers → paper landing page → DOI or preprint. Also the citation/BibTeX copy.
2. Policymakers and journalists → policy report → Taub page or PDF. Also the contact email.
3. Event organisers and media → Media page and short/long bios → email.
4. Students → Teaching page → open resources, guidebooks.

Primary call to action: **Explore research**. Secondary: **Read policy analysis**. Tertiary: **Get in touch**. There is no newsletter and no contact form, because neither exists.

## Information architecture (as built)

```
docs/
├── index.html            Home: hero + diagram · credentials · 3 pillars · 4 selected papers · 3 policy reports · media · latest · contact
├── research.html         Agenda · themes (question/approach/why/key work) · 6 selected · full bibliography (static + JS filters) · profiles & data
├── publications/<slug>/  28 landing pages: summary, details, cite/BibTeX, related work, Highwire + ScholarlyArticle metadata
├── policy.html           13 Taub reports in 4 theme groups (chip filter) · policy↔research bridge
├── media.html            Video (click-to-load) · radio · opinion · press · talks (chip filter), original-language titles
├── teaching.html         Institutions · guidebooks · guest lecture · open resources for students
├── about.html            Bio · at-a-glance facts · short/long bios (copy) · profiles · contact
├── 404.html              Self-contained; links resolve on root or GitHub project path
├── data/                 publications.json · publications.bib · policy.json · media.json
├── css/site.css · js/site.js · js/bibliography.js · fonts/ (OFL) · img/favicon.svg
└── robots.txt · .nojekyll  (sitemap.xml generated once the domain is known)
```

Navigation: Research · Policy · Media · Teaching · About · Contact (→ about.html#contact). The same header and footer appear on every page. Paper pages mark "Research" as current.

## Wireframes (representative)

**Home, desktop (≥900px)**
```
┌──────────────────────────────────────────────────────────────────────┐
│ [■▨] Labib Shami / ECONOMIST        Research Policy Media Teaching About (Contact) │
├──────────────────────────────────────────────────────────────────────┤
│ ECONOMIST · TAUB CENTER …            │  ┌Central bank┐   ┌Government┐  │
│ Labib Shami                          │        ↘ money   taxes ↗        │
│ לביב שאמי · لبيب شامي                 │       ┌Households & firms┐       │
│ Studying the economy that official   │  recorded ↙        ↘ unrecorded │
│ statistics record, and the part …    │  ┌Observed┐ ⇠cash⇢ ┌▨Non-obs.▨┐ │
│ lede…                                │  caption (original illustration) │
│ (Explore research) (Read policy) →   │                                  │
├──────────────┬──────────────┬──────────────┬─────────────────────────┤
│ CURRENT ROLE │ FACULTY      │ DOCTORATE    │ ORCID                   │
├──────────────────────────────────────────────────────────────────────┤
│ 01 RESEARCH — Three lines of inquiry   [card] [card] [card]          │
│ 02 Selected research (editorial list: year · title · venue · summary · links) │
│ 03 Policy analysis [report] [report] [report]                         │
│ 04 In public [video facade] | [media list with original titles]      │
│ 05 Latest (6-item timeline)                                          │
│ 06 Contact band (email, bios)                                        │
│ Footer                                                               │
└──────────────────────────────────────────────────────────────────────┘
```

**Research → bibliography, mobile (360px)**
```
┌───────────────────────┐
│ [■▨] Labib Shami (Menu)│
│ RESEARCH               │
│ Research & publications│
│ lede…                  │
│ [Search ……………]        │
│ [Type ▾] [Theme ▾]     │
│ [Order ▾] (Reset)      │
│ Showing all 28 works   │
│ 2026 ───────────────── │
│ [OPEN ACCESS]          │
│ Title (link)           │
│ Authors (Shami bold)   │
│ Venue vol(issue), pp   │
│ Summary · DOI ↗ · …    │
│ ─────────────────────  │
└───────────────────────┘
```

**Paper landing page**
```
Breadcrumb · TYPE · YEAR · Title (h1) · Authors · Venue + badges · [Read the article ↗] [Preprint ↗]
┌ Summary (lede) + provenance note ┐ ┌ Details (dl) ┐
│ Research theme chips             │ │ Cite (APA) [Copy] │
│ Related publications / policy    │ │ ▸ BibTeX [Copy]   │
└──────────────────────────────────┘ └───────────────────┘
```

## Phase 2 (not built; needs input)

- Hebrew and Arabic pages (`/he/`, `/ar/`) with `dir="rtl"`. Human translation only.
- Approved portrait and a downloadable current CV.
- Full-text HTML editions of the CC BY articles, after author review.
- Canonical URLs, `og:image`, `sitemap.xml` once the domain is chosen.
