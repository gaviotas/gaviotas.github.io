# Design

## Current direction
- Active: 2026-10-09. User explicitly requested Meng Chen's actual template with their personal information, rather than mixing the previous custom design with a reference.
- Source: https://github.com/Casardo-Chen/casardo-chen.github.io at `a09f1557c94e567f7ab693cd59f39794b330c3a8`.
- Original `BaseLayout`, `BaseHead`, `Header`, `SideBar`, `SideBarFooter`, `SideBarMenu`, `Footer`, `HorizontalCard`, `HorizontalCard.scss`, `global.css`, and Tailwind configuration were copied from that repository.
- Actual template look: `lofi` DaisyUI theme, #f9f9f9 main background, #444 text, #3b60d9 links, Avenir/system sans typography, 19rem sidebar, 865px main width, 13rem research previews, round profile image, mobile checkbox drawer.
- The previous ivory/green CSS, custom DM Sans font, custom rail, anchor navigation, and custom drawer script were removed. Do not reintroduce that visual layer without a new user direction.

## Content and navigation
- Personal content remains in `_data/*.yaml`, bundled at build time. Static assets are under `public/assets/`.
- About: three paragraphs ordered by research question, academic background/mentors, and current industrial work. Preserve Prof. Hyunjung Shim and mentors Song Park, Byeongho Heo, Dongyoon Han. Use original bold and number-list inline emphasis for the research focus, limited supervision, and compact representations.
- Homepage uses Featured Projects, following the user’s 2026-10-10 direction, with a curated first/co-first-author selection in profile.featured_publications. All 12 papers remain on Publications. Publications groups conference proceedings, journal articles, and preprints with original-style collapse controls.
- Separate pages: About `/`, Publications `/publications/`, Experience `/experience/`, Awards `/awards/`, Contact `/contact/`.
- Experience: 5 entries, existing mentors and small organization logos. Awards: 3 plain entries. Publications includes a Patents section with 1 entry.
- Email: mh315.lee@samsung.com. No CV link, ML monogram, or reviewer activity section.
- All 12 previews use original paper figures or author-maintained homepage/repository images. The EPS++ and NCLS concept overviews were replaced with original figures from author-provided PDFs on 2026-10-10. Provenance in `public/assets/research/SOURCES.md`.

## Compatibility adaptations
- Astro 7 replaces original Astro 2. Tailwind 3 and DaisyUI 3 retain the original template's class/theme behavior.
- Legacy `@astrojs/image` calls were replaced with native image tags using local media, dimensions, lazy loading, alt text, and contain sizing.
- Author HTML comes from the existing local YAML rather than Meng Chen's author-name array. Personal links replace the original social accounts.
- Small accessibility-only stylesheet provides skip link, focus, reduced motion, social control sizing, and overflow fixes; it does not recolor or redesign the template.
- Original MIT notice retained in `licenses/Astrofy-MIT.txt`.

## Validation
- Static build, HTTP routes/assets, source comparison, and whitespace checks are available. Browser screenshot/interaction verification remains unavailable; do not claim rendered desktop/mobile validation.
- Local Astro server: http://127.0.0.1:4000. GitHub Pages uses Node and `dist/`.

## Author names
- Display all publication authors with their verified full names, in source order. Minhyun Lee is bold and underlined as in the original template; preserve existing equal-contribution and corresponding-author markers.
- Author-line overrides in `_data/publication_authors.json` prevent Scholar imports from restoring abbreviations. Seonho Lee and Seungho Lee are distinct authors.

## Venue labels
- Use the original Meng Chen card’s italic full venue line followed by a bold abbreviation/year line. Homepage uses only the short venue as in Meng Chen’s original; Publications shows both lines. Display names and year templates are in `_data/publication_venues.yaml`; original citation metadata stays intact.

## Template spacing fidelity
- About uses inline text-lg runs separated by two line breaks, matching the original rather than block paragraphs with mt-5.
- Preserve original main sizing and compact publication resource links; do not add a 44px minimum height to paper links, which changes row rhythm.

## Featured Projects selection (2026-10-10)
- Newest-first: MaskRIS (TMLR 2025), SeiT++ (ECCV 2024), AMN (CVPR 2022), EPS (CVPR 2021); all have Minhyun Lee as a first/co-first author.
- Google Scholar profile retrieved directly on 2026-10-10: EPS 402 citations, AMN 143, PsyNet 44, EPS++ 38, HybridMatch 13, SeiT++ 5, MaskRIS 4. Counts are a dated selection reference, not displayed or automatically updated.
- Selection balances established citation impact (EPS/AMN), storage-efficient representation learning (SeiT++), and vision-language segmentation (MaskRIS). EPS++ overlaps the EPS research line; PsyNet and HybridMatch cover older localization/landmark work.
- Keep the curation independent of publication array positions and Scholar imports. This supersedes the previous no-Featured label direction for the homepage only.

## Contact
- Lead with a welcoming invitation to questions, discussions, and coffee chats and a body-size email address. Use quiet horizontal rules, a mailto address with an adjacent small copy icon, and an editorial list of external profiles with descriptions and outward arrows.
- Preserve original template colors and type; avoid cards, fabricated office/location details, or unsupplied claims of collaboration availability. Copy feedback is announced, with text-selection fallback; mailto works without JavaScript.

- Contact accents: original number-list highlights for questions/discussion, blue coffee-chat text with a small outlined cup, matching mail icon, and monochrome profile logos reused from the sidebar SVGs (public/assets/icons). Keep the email at body size.

## Awards
- Editorial list with thin horizontal rules, small blue outlined trophy/medal icons, and selective blue emphasis on award distinctions. Dates align right on larger screens and below the text on small screens. Preserve all three factual titles/descriptions; no cards, date badges, oversized trophies, or invented achievement descriptions.

## Website dates
- Repository created and initial commit: 2024-01-03 (GitHub API and git history). Sidebar shows Created: Jan 3, 2024 and a manually maintained last-content-update date from main_info.yaml. Footer copyright starts in 2024. Do not use a rebuild date as a content-update date. Exact first public deployment has not been established.

- Patents reuse HorizontalCard: plain bold title, full inventor names with Minhyun Lee bold/underlined, italic details, bold patent reference/year, and Patent resource link. Section heading/collapse controls match publication categories; no placeholder thumbnail. Inventors verified against https://patents.justia.com/patent/11798171.

- Featured Projects only: render two non-interactive topic tags below each title, using blue text on a pale blue background. Keywords live in profile.featured_keywords; full Publications retains citation-only cards.

## Experience hierarchy
- Each entry separates role/degree (bold text-lg), organization (body size), and dates (muted text-sm). Former organization names use a separate former_name field and a quiet inline note. Preserve original timeline, organization logos, and mentor links.

## Featured thumbnail frames
- Featured Projects use 13rem-wide 16:9 white frames with .25rem inset and contain sizing, matching the original compact template dimensions. The larger 15rem/4:3 variant was rejected by the user. Click opens the original full-size figure in a new tab.
- Original image files and full-publication 13rem/16:9 styling remain intact. Differing figure proportions naturally leave different whitespace; do not crop diagrams to force equal content height.

## Social sharing
- Default Open Graph/Twitter preview is public/assets/social/preview.png (1200×630), rendered from its SVG source. Typography, #f9f9f9 background, and blue accent follow the site. Include name, research headline, verified role/affiliation, and canonical domain.
- Share titles include the owner’s name on every route; image URLs are absolute. Preview becomes publicly accessible only after deployment.

## About motion
- One focal moment beside the research headline: seven scattered observations settle into a sparse 3×3 structure, leaving two outlined gaps. Blue SVG is 48px (40px mobile).
- CSS-only .8s movement and line drawing run once per page load; no looping, hover replay, dependency, or delayed content reveal. Static final geometry is the fallback and reduced-motion state. Decorative SVG is hidden from assistive technology.

## Supporting icons
- Contact coffee icon is static at 18px; Awards icons are static at 24px. Hover animations and the enlarged 32px variant were removed at the user’s request. The About headline motif remains unchanged.

## Color refinement (2026-10-10)
- Keep the Meng Chen palette: #f9f9f9 canvas, #f2f2f2 highlight/sidebar surfaces, #3b60d9 accent, #e6e5e5 dividers.
- Topic tags now use the same gray highlight background as About. Headings/name use #222, body/menu #444, secondary text/sidebar dates #666. The active menu uses darker text and a slightly stronger weight.
- Contact profile names use body color; arrows and existing accent icons remain blue. Global heading color and sidebar text hierarchy are intentional refinements to the original stylesheet.

- Author markers (* equal contribution, † corresponding author) use shared superscript styling at 75% size with zero line-height, preserving the author-line spacing and Scholar-import HTML.

- Featured Projects links to the full list with “View all publications”, blue text, a thin underline, and a small forward arrow. Keep it a lightweight text link beside the heading with wrapping on narrow screens.

- Publications/Patents section controls use small outlined circular chevrons (28px visual, 44px target). Down means expanded; right means collapsed. ARIA labels and expanded state track the section; reduced-motion settings suppress the short rotation transition.

- Featured frames position the image absolutely within the inset, so tall intrinsic image dimensions cannot stretch the 16:9 frame. Contain sizing preserves the complete figure; overflow is bounded by the frame.

- Sidebar email: body-colored small text with a 16px blue envelope and quiet underline. Add a small separation from affiliation; retain mailto and a 44px click target. No filled button or oversized address.

## Light / dark themes (2026-10-10)
- The top-right sun/moon slider appears on desktop and mobile. Keyboard-operable switch, 44px height, visible focus, and reduced-motion support; no added dependency.
- Initial theme defaults to light regardless of the OS setting; explicitly selected dark mode is remembered. Store the choice in localStorage; apply it inline before paint, retain across pages, and sync between tabs. Storage failure retains switching for the current page.
- Light keeps the original palette. Dark uses #191b20 canvas, #22252c surfaces, #363b45 dividers, #f1f2f5 headings, #d3d6dc body, #a8aeb9 secondary text, and #95afff accent.
- Shared CSS roles cover page text, links, keywords, awards, contact, timeline, sidebar, focus, selection, and resource states. DaisyUI uses matching dark surfaces; research thumbnails remain white, brand logos use a small light backing, monochrome contact logos invert.

- Theme slider motion: accent-filled 32px thumb slides over 420ms with subtle settling, while sun/moon icons rotate slightly and change emphasis. Keep the 76×44px control size; CSS transitions can reverse during rapid toggles, and reduced-motion changes state immediately.

- Dark-mode sun icon retains full opacity and full 16px size, with heading-color contrast and a 1.8px stroke; inactive must remain clearly discoverable.
- Theme icons now have small expressions: round smiling sun and sleepy crescent moon, 18px with rounded strokes. Keep both at full size; only a gentle 12-degree rotation accompanies switching. This replaces the previous 16px / 45-degree sun treatment.
- Experience logo sizing: company wordmarks share a 6.5rem width and natural aspect ratio; university seals use 2.5rem square dimensions. At ≤480px, use 5.5rem / 2.25rem respectively to leave more room for text. Placement and theme treatment remain unchanged.

- Experience uses official color variants at full opacity: Samsung Blue #1428A0, NAVER green, Yonsei blue seal. Preserve the newly balanced sizes and current dark-mode light backing. Asset provenance is in organizations/SOURCES.md.

- Featured thumbnail clicks now open the paper landing page (paper.paper_pdf, same destination as Paper) in a new tab, replacing the full-size figure link. Preserve thumbnail sizing; link labels announce the destination and new tab.
- Featured thumbnail frames use 6px rounded corners, a thin border, and a 200ms border-color transition to accent on hover/focus. Dark mode uses #89909c for the frame border; keyboard focus adds a 2px outline with 4px offset. Existing 13rem/16:9 dimensions, image containment, and new-tab paper destinations stay intact. Global reduced-motion disables the transition.

- About prose affiliations (Yonsei University, NAVER AI Lab, Samsung Electronics AX/PI Center) use medium-weight teal text with a subtle teal background: #256c68 on #e7f1ee in light, #8acbc3 on #243b3a in dark. Match research highlight padding and 4px corners; clone the decoration when an affiliation wraps. Research topics retain the blue number-list highlight; mentor links retain their existing blue. Sidebar and Experience affiliation styling stays unchanged.

- Featured preview width follows Publications on mobile: 100% of the image column below 768px, 13rem from 768px upward. Keep the 16:9 contained image, rounded border, and paper-page link.
