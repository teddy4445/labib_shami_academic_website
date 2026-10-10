# Website brief: Dr. Labib Shami

## Strategic idea

Position Labib as an economist working across **economic theory, computational modeling, and policy-relevant evidence**. The main audience paths are academic researchers, policymakers, media/speaking organizers, and students. Never turn the website into a CV wall or an uncritical news aggregator.

## Candidate hero (copy to approve)

**Labib Shami**  
**Economics, policy, and the forces shaping everyday life.**  
Research on monetary policy, the non-observed economy, and the economic choices affecting households, businesses, and governments.

Two hero actions: **Explore research** / **Read policy analysis**. Secondary contact action.

## Page map

1. `index.html`: hero, institutional credentials, 3 research pillars, 4–6 featured works (academic + policy), featured video/podcast, contact.
2. `research.html`: areas explained, filtered academic bibliography, papers with DOI, years, topics and verified author lists. Publication links always work with JS disabled.
3. `policy.html`: Taub reports by year, thematic cards on inflation/cost of living, credit/housing, SMEs, macroeconomic trends.
4. `media.html`: authored essays, interviews, hosted videos and audio, public lectures. Include original outlet and date, not copied thumbnails.
5. `teaching.html`: books and academic teaching; only show specific course syllabi after supplied/verified; no invented courses.
6. `about.html`: approved short and long bio, education, research background, links to verified external profiles, professional contact.
7. Optional `paper/<slug>.html`: create only for papers with reliable metadata; full HTML body only with correct permission and meticulous correction.

## Editorial pillars

- **Monetary policy and household finance:** banking, credit, inflation, housing, cash and consumer debt.
- **The informal economy and economic modeling:** non-observed economies, tax evasion, monetary equilibrium, machine learning, agent-based models.
- **Socioeconomic policy and resilience:** Israel macroeconomy, SMEs, local policy, crisis economics, economic-epidemiological interactions.

## Visual direction

Academic editorial with applied-policy visual cues. Prefer near-white backgrounds, graphite/navy type, restrained teal accents, warm highlights for charts, generous whitespace, elegant serif headings and clean sans body. Avoid an agency-like sales landing page. Use charts from confirmed public data or clear original conceptual figures; no copyrighted institutional graphics without permission. Avoid fake paper cover illustrations that look like journal facsimiles.

## Multilingual growth plan

Phase 1 English with exact original Hebrew/Arabic titles and `lang` attributes. Phase 2 actual translated pages with direction `dir=rtl`, tested with proper bidirectional typography and menus. Never machine-translate academic claims into public pages without human review.

## Technical constraints

- Deployable `site/`: pure HTML5/CSS/JS; no Node, no npm, no bundler, no backend.
- Optional Python scripts for **offline editorial preparation only** outside `site/`.
- No runtime reliance on proprietary API keys or scraping academic catalogs.
- Publications content from version-controlled local JSON, accessible as static HTML as well.
- Semantic headings, alt text, keyboard navigation, skip link, prefers-reduced-motion, WCAG AA contrast, metadata/schema.org, sitemap, robots, OG tags.
- GitHub Pages base-path safety (`./` relatives or configured base path).
- Pass broken-link checks, Chrome or Playwright screenshots, 320/768/1440px reviews, mobile menu interaction and JS-disabled checks.

## Conversion goals

Academic visitor: paper view/download → DOI/repository.  
Policy visitor: report or policy finding → source.  
Media visitor: expertise and speaking clips → verified contact.  
Student visitor: teaching/book materials → course/resources links.
