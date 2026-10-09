# Design

## Source of truth
- Status: Active
- Last refreshed: 2026-10-07
- Primary product surfaces: English personal academic homepage at `/`.
- Evidence reviewed: `README.md`, `index.html`, `_layouts/default.html`, `_data/`, `libs/custom/my_css.css`, current typography, diagrams, institution assets, and user feedback. A rendered screenshot baseline is not available.

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
- Use warm neutral text with one restrained green link accent and preserve the data-driven Jekyll structure.
- Make reading and navigation easier at every width.
- Group the complete bibliography by year; use consistent styling for every paper.

## Visual language
- Color: Warm ivory background (#f8f7f3), dark green-gray text (#26352f), muted metadata (#626b64), and one forest-green link/focus accent (#285c4d), coordinated with the existing harbour photograph.
- Typography: System sans-serif body at 16px, metadata at least 14px, publication titles at 18px. Georgia name at 44–76px and section headings at 27–30px provide a distinct editorial hierarchy; the research headline is 24–30px, with a short central statement.
- Layout: Maximum 1040px. Desktop sections pair a 176px title column with the content column; at 749px and below, headings sit above their content. Publications keep uniform year groups and resource links. Ample space separates sections; fine rules separate records.
- Shape: Existing photograph in a subtly angled white mat, with an offset sage backing and small location caption. Geometric annotation marks surround the photograph; no shadow.
- Motion: Reduced-motion-aware smooth navigation and subtle link color transitions; no decorative entrance animation.
- Imagery: Existing environmental portrait at 320px including its mat on wide desktop and 180px on narrow phones. Preserve its full composition. Three conceptual SVG diagrams remain geometric cues, not scientific results.
- Display type: Georgia for the name, research headline, section titles, and footer signature; system sans-serif for detailed research and career content.

## Components
- Reuse: Portrait, section navigation, publication data, visible focus and skip link.
- Change: Name leads the profile without an eyebrow or duplicate identity bar. The short headline states the research question; About connects it to current work; three concise research themes give concrete examples. Resource links use shared functional icons; academic background and mentor links live in Experience.
- States: Hover, keyboard focus, section anchor target and navigation current-section indicator.
- Ownership: `libs/custom/my_css.css` owns overrides and tokens; `_data/` owns content.

## Accessibility
- Target: WCAG 2.2 AA-informed implementation; full conformance is not established by this change.
- Keyboard: Visible focus for every link; skip link to main content.
- Readability: Preserve contrast; enlarge compact labels and controls.
- Scrolling: Root scroll padding accommodates the sticky navigation for heading links and keyboard focus. Respect native page zoom and scrolling.
- Semantics: One h1, h2 section headings, h3 year headings, h4 paper headings inside year groups; patents use h3.
- Motion: No dependency on animation or hover to reveal information; respect reduced-motion preferences for scrolling.

## Responsive behavior
- Support narrow phones through desktop without fixed-width content overflow.
- Header: Name and research headline beside a matted portrait on desktop; compact portrait follows the profile copy on narrow phones. Name and headline sizes decrease progressively with width.
- Navigation: Wrapping links on mobile, sticky row from 750px; anchor spacing accounts for the sticky bar.
- Experience and awards: Experience dates sit beside content from 1000px and above, then above content at narrower widths. Award dates sit to the right, then below the title/details on phones. A thin career spine and small markers connect experience entries; awards use compact text rows with quiet dates and fine separators.
- Touch: Links with approximately 44px minimum control height and spaced icon targets.

## Interaction states
- Loading: Static HTML remains readable while fonts load.
- Empty: Optional email/social links are rendered only when configured.
- Error: Missing assets must be identified during build verification.
- Success: Section links reach headings, paper links open publications and email uses mailto.
- Disabled: Not applicable.
- Slow network: System font fallback; content and section links work without JavaScript. The current-section indicator is progressive enhancement.

## Content voice
- Tone: Concise, factual first-person English. The central question is learning from imperfect data. Keep educational history and mentor details in Experience; connect research to current industrial applications in About.
- Research themes explain the questions behind the publication list; do not invent interests, project outcomes or impact claims.
- Preserve publication titles, author attribution and existing research claims.
- Label undated publications as Preprints instead of displaying a year of zero.

## Implementation constraints
- Jekyll/Liquid and local CSS; no new dependencies or external font requests.
- Keep Google Scholar importer output compatible.
- Exclude this brief from published assets.
- Validate build, rendered content, heading structure and CSS; screenshot verification requires a connected browser.
- Refinement tools: Impeccable 4.5.0 and Vercel web-design-guidelines, installed outside this repository. Apply their relevant guidance under this brief; avoid hooks, frontend packages, or external font dependencies.

## Open questions
- Google Scholar direct HTTP retrieval succeeded on 2026-10-05 after the web tool returned HTTP 429. Observed citation counts: Railroad Is Not a Train (EPS) 402; Threshold Matters 143; PAMI Saliency 37; SeiT++ 5; MaskRIS 4. Profile: https://scholar.google.com/citations?user=2hUlCnQAAAAJ&hl=en&cstart=0&pagesize=100.
- [ ] Owner: reviewer. Check rendered desktop/mobile screenshots when a browser becomes available.

## Current refinement
- User feedback: Previous spacing and alignment changes did not create enough visual distinction. Maintain simple & professional while making the page feel deliberately designed.
- Direction: Warm editorial academic portfolio, led by the personal photograph and serif typography, with a consistent section-title rail. No new factual claims, selected-paper emphasis, CV links, or reviewer list.
- Validation: Local Jekyll build and HTTP serving can be checked. A connected browser is still required for desktop/mobile visual confirmation.
- Latest feedback: Keep the approved colors, but add visible graphic character. The portrait now has sparse-point, contour, and orthogonal layout geometry; these are conceptual decoration, hidden from assistive technology, not scientific results. Research focus occupies a full-width sage band with larger diagrams and unboxed columns. A restrained experience spine adds chronological rhythm. No new content claims or dependencies.

## Personal identity and icons
- User decision: No ML monogram. The hero name is the primary identity, with the original PNG favicon. Keep functional link icons.
- A local SVG include owns an 18px, 1.6px-stroke icon family for email, scholarly profiles, code, documents, and navigation. Icons accompany visible text and are hidden from assistive technology. Profile icons are functional symbols rather than a claim to official brand artwork.
- No duplicate identity row or redundant Publications shortcut. Preserve 44px link targets and the existing palette. No icon font, package, remote request, or image generation is needed.

## Awards treatment
- Small type, fine separators, and quiet dates. No emblems, colored award backgrounds, or display typography: earlier treatments were too ornate for the user.
- Explain AIC as AI Center in the institution line. Keep the award names unchanged; their internal significance has not been confirmed and must not be invented.

## Experience logos
- Use locally stored Samsung, NAVER, and Yonsei assets from their official websites. Preserve original colors and aspect ratios; sources are recorded in `assets/organizations/SOURCES.md`.
- User correction: The colored left-side logos felt visually inconsistent. Use official monochrome variants as small supporting marks to the right of institution names. Samsung uses its transparent header wordmark instead of the blue square. Institution names, roles, and descriptions share a single left edge. Logos have empty alt text because adjacent headings already identify the organization; images are lazy-loaded with intrinsic dimensions.

## Date typography
- User correction: Separate, enlarged year/month stamps felt excessive. Use quiet 13px sans-serif dates in muted gray, on a single line where space allows (Apr 2026; Dec 2024 – Present).
- Experience dates may wrap naturally on narrow date rails. Keep ISO month fields and semantic `<time>` elements; do not add special year colors, display fonts, backgrounds, or badges.

## Advisor and mentor attribution
- User preference: Include Prof. Hyunjung Shim and NAVER mentors Song Park, Byeongho Heo, and Dongyoon Han in the About research narrative, with their existing homepage links. Their attribution may also remain in Experience; do not remove it merely to reduce repetition.

## Content refinement after review
- About uses three paragraphs: current role and research question; concrete academic research and NAVER training work; current industrial application and the connecting theme. The user prefers a fuller narrative over the earlier two-paragraph summary. Experience owns degree, advisor, mentor, and date details. Research themes remain short, concrete examples. Publications has no redundant research-summary paragraph.
- Current Samsung work is described as semiconductor data modeling and layout generation, without additional claims about reliability, deployments, or impact.
- Publication venues use concise labels from `_data/publication_venues.yaml`; the original metadata is retained. Title corrections also live in Scholar import overrides so a future import preserves casing and linked resources. No import was run.
- Verified title casing: [Threshold Matters](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Threshold_Matters_in_WSSS_Manipulating_the_Activation_for_the_Robust_CVPR_2022_paper.html), [Railroad Is Not a Train](https://openaccess.thecvf.com/content/CVPR2021/html/Lee_Railroad_Is_Not_a_Train_Saliency_As_Pseudo-Pixel_Supervision_for_CVPR_2021_paper.html), [PsyNet](https://ojs.aaai.org/index.php/AAAI/article/view/6615), and IEEE-supplied Crossref metadata for [HybridMatch](https://doi.org/10.1109/ACCESS.2023.3257180) and [Saliency](https://doi.org/10.1109/TPAMI.2023.3273592).
- Browser verification remains unavailable; the user confirmed Chrome is not installed. Do not install a browser or claim screenshot validation as part of this refinement.
