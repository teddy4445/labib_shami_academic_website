# Design direction: "Ledger"

**Metaphor:** an editorial monograph with the restraint of a policy brief. One motif carries the research identity: **solid vs hatched**, for the observed vs the non-observed economy. It appears in the logo mark, favicon, hero diagram and pillar glyph.

**Attributes:** rigorous · lucid · grounded · multilingual · quietly distinctive.

## Colour (CSS custom properties in `css/site.css`)

| Token | Light | Dark | Role | Contrast vs paper |
|---|---|---|---|---|
| `--paper` | #F7F5F0 | #0F161D | Canvas | — |
| `--paper-2` | #EEEAE1 | #16202A | Tinted bands | — |
| `--ink` | #15202B | #E9E5DC | Text | 15.1 : 1 / 14.5 : 1 |
| `--ink-2` | #465260 | #AEB7C1 | Secondary text | 7.3 : 1 / 9.0 : 1 |
| `--navy` | #1D3A5C | #9CC2EA | Links, primary buttons | 10.6 : 1 / 9.8 : 1 |
| `--teal` | #0E6B66 | #6CC7BE | Eyebrows, observed flows, focus ring | 5.8 : 1 / 9.2 : 1 |
| `--ochre` | #9A5A17 | #E3A15E | Years, tags, non-observed flows | 5.0 : 1 / 8.3 : 1 |

Neutrals carry about 80% of the surface. Navy is used for actions and teal/ochre only for small accents. Every text pairing meets WCAG AA, as checked by script and by axe-core in light and dark mode.

## Typography

- **Newsreader** (variable, optical sizes) for display and headings, the hero statement, years and summaries. It gives an editorial, newspaper-like voice suited to economics and policy.
- **Source Sans 3** (variable) for body text and UI.
- Hebrew and Arabic text uses system fonts with `lang`/`dir` (Noto, Arial Hebrew, Geeza Pro, Segoe UI and Tahoma fallbacks).
- Both fonts are self-hosted, latin plus latin-ext subsets, under the OFL. There are no external font requests.
- Fluid scale from `--step--1` to `--step-5` using `clamp()`. Body text is 17–18px with a reading measure of about 68ch.

## Layout and components

- `wrap` is 1180px max with fluid gutters. Sections use generous vertical rhythm (`--space-8`) and are separated by thin rules or tinted bands.
- Numbered eyebrows ("01 Research") give long pages a report-like structure.
- Components: hero + diagram, credentials strip, pillar cards with evidence lists, editorial work list (year column), report cards, bibliography entries with badges, paper detail/cite panels, media rows with original-language titles, video facade, timeline, contact band, facts list, link list.
- Badges: Open access (teal), Preprint (ochre), Online first (navy), Book chapter (grey). Each pairs text with colour, so colour is never the only signal.

## Imagery

- No portrait was authorised, so the hero uses an original conceptual SVG diagram (central bank, government, households & firms, observed and non-observed economies). It is captioned as original and not taken from a paper.
- There are no stock photos, fake journal covers, institutional logos or copied thumbnails. The video facades are typographic, and the guidebooks are shown as abstract CSS spines.

## Interaction and motion

- Mobile menu below 860px. The toggle uses `aria-expanded`, and Escape, an outside click or following a link closes it.
- Bibliography: search, type, theme, order and reset controls; live count; URL state; empty state. The full list is static HTML, so the page works without JavaScript.
- Chip filters on Policy and Media use `aria-pressed` and stay hidden without JavaScript.
- Copy buttons (citation, BibTeX, bios) fall back to text selection if the Clipboard API is unavailable.
- Transitions are hover-only and limited to about 0.15s. All motion is disabled under `prefers-reduced-motion`.

## Mobile adaptation

- Single column throughout. On small screens the hero diagram drops its sub-labels and enlarges its labels.
- The credentials strip stacks, work list links wrap under the text, and bibliography controls stack.
- Tap targets are at least 40–46px tall.
