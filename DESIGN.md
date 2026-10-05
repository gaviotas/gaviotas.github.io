# Design

## Source of truth
- Status: Active
- Last refreshed: 2026-10-05
- Primary product surfaces: English personal academic homepage at `/`.
- Evidence reviewed: `README.md`, `index.html`, `_layouts/default.html`, `_data/`, `libs/custom/my_css.css`, Skeleton and timeline CSS. No existing design brief or screenshot baseline was found.

## Brand
- Personality: Simple & professional; clear, restrained, research focused.
- Trust signals: Accurate affiliation, publications, patents, awards and experience.
- Avoid: Decorative motion or dense dashboards.

## Product goals
- Help visitors understand current research, find papers and contact the researcher.
- CV links are excluded at the user's request.
- Success signals: Research focus and email are discoverable in the header; sections are reachable on phones and with a keyboard.

## Personas and jobs
- Assumed primary visitors: Researchers, collaborators and professional contacts.
- Jobs: Scan research interests, find publications/code and read career history.
- Contexts: Desktop and mobile, including keyboard and assistive technology use.

## Information architecture
- Navigation: About, Publications, Patents, Awards, Experience.
- Route: One page with section anchors.
- Hierarchy: Profile and research focus; introduction; publications grouped by year; patents; awards; experience.
- User decision: Display all papers uniformly, without selected-paper labels, backgrounds or borders.

## Design principles
- Use neutral text with one restrained link accent and preserve the data-driven Jekyll structure.
- Make reading and navigation easier at every width.
- Group the complete bibliography by year; use consistent styling for every paper.

## Visual language
- Color: White background, dark neutral text, gray metadata, one blue link/focus accent.
- Typography: System sans-serif stack; body 16px, metadata at least 14px, name 38–48px, section headings 22–24px and paper headings 17–18px. Give the profile headline a deliberate display treatment.
- Layout: Maximum 920px for the header/navigation and 800px for prose/publications; consistent section spacing. Small monospace section indices and dates provide an editorial rhythm.
- Shape: Fine rules and a restrained offset portrait frame; no heavy shadows.
- Motion: Smooth section navigation only when reduced motion is not requested.
- Imagery: Existing environmental portrait at 228px on desktop, preserving its full composition. Three small abstract SVG diagrams illustrate supervision, representations and layout patterns. These are conceptual visual cues, not scientific results.
- Display type: Use Georgia only for the research headline, with the system sans-serif stack for names and body copy.

## Components
- Reuse: Portrait, section navigation, publication data, visible focus and skip link.
- Change: Compact profile header, factual personal narrative and three research themes, text resource links, dated award/experience lists.
- States: Hover, keyboard focus, section anchor target and navigation current-section indicator.
- Ownership: `libs/custom/my_css.css` owns overrides and tokens; `_data/` owns content.

## Accessibility
- Target: WCAG 2.2 AA-informed implementation; full conformance is not established by this change.
- Keyboard: Visible focus for every link; skip link to main content.
- Readability: Preserve contrast; enlarge compact labels and controls.
- Semantics: One h1, h2 section headings, h3 year headings, h4 paper headings inside year groups; patents use h3.
- Motion: No dependency on animation or hover to reveal information; respect reduced-motion preferences for scrolling.

## Responsive behavior
- Support narrow phones through desktop without fixed-width content overflow.
- Header: Name and research headline beside a framed portrait on desktop; portrait above text on narrow phones. Keep its footprint compact on phones.
- Navigation: Wrapping links on mobile, sticky row from 750px; anchor spacing accounts for the sticky bar.
- Experience and awards: Date column beside content on desktop; dates above content on phones. No timeline markers or colored badges.
- Touch: Links with approximately 44px minimum control height and spaced icon targets.

## Interaction states
- Loading: Static HTML remains readable while fonts load.
- Empty: Optional email/social links are rendered only when configured.
- Error: Missing assets must be identified during build verification.
- Success: Section links reach headings, paper links open publications and email uses mailto.
- Disabled: Not applicable.
- Slow network: System font fallback; content and section links work without JavaScript. The current-section indicator is progressive enhancement.

## Content voice
- Tone: Concise, factual first-person English. Connect academic research on imperfect supervision to current industrial data and layout generation work.
- Research themes explain the questions behind the publication list; do not invent interests, project outcomes or impact claims.
- Preserve publication titles, author attribution and existing research claims.
- Label undated publications as Preprints instead of displaying a year of zero.

## Implementation constraints
- Jekyll/Liquid and local CSS; no new dependencies or external font requests.
- Keep Google Scholar importer output compatible.
- Exclude this brief from published assets.
- Validate build, rendered content, heading structure and CSS; screenshot verification requires a connected browser.

## Open questions
- Google Scholar direct HTTP retrieval succeeded on 2026-10-05 after the web tool returned HTTP 429. Observed citation counts: Railroad Is Not a Train (EPS) 402; Threshold Matters 143; PAMI Saliency 37; SeiT++ 5; MaskRIS 4. Profile: https://scholar.google.com/citations?user=2hUlCnQAAAAJ&hl=en&cstart=0&pagesize=100.
- [ ] Owner: reviewer. Check rendered desktop/mobile screenshots when a browser becomes available.
