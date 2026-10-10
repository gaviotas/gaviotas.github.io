# Minhyun Lee Website

Personal academic website built with [Astro](https://astro.build/) and deployed to GitHub Pages.

The site was migrated from Jekyll to the actual template from [Meng Chen's academic website](https://meng-chen.com/) and the [Astrofy](https://github.com/manuelernestog/astrofy) template. The source layout, Tailwind/DaisyUI theme, typography, and research cards are retained; personal information comes from Minhyun Lee’s YAML data.

## Local development

Requires Node.js 22.12 or later.

```bash
npm ci
npm run dev
```

Astro serves the local site at `http://127.0.0.1:4000` (configured in `astro.config.mjs`).

## Production build

```bash
npm run build
npm run preview
```

The generated static site is written to `dist/`.

## Deployment

Pushes to `main` deploy through [`.github/workflows/astro.yml`](.github/workflows/astro.yml). The workflow can also be started manually from GitHub Actions.

## Content

Edit `_data/*.yaml` for profile, publications, awards, and experience. Publication previews and summaries live in `_data/research_media.yaml`; static images are in `public/assets/`. Keep canonical publication titles aligned with research media keys.

The existing `scripts/import_scholar.py` still writes `_data/publications.yaml`. Run it deliberately: it uses network access and may replace manual publication metadata.

## Attribution

See `licenses/README.md` and `licenses/Astrofy-MIT.txt` for reference code attribution. Image sources are documented alongside the assets.

## Template provenance

The reference repository’s original layout, sidebar, header, footer, research card, and styles are used directly. Astro 2 image components are adapted to native image tags for Astro 7. `DESIGN.md` records the source revision and compatibility changes. The small `accessibility.css` file adds access/overflow fixes without replacing template styling.

Verified full-name author lines live in `_data/publication_authors.json`. The Scholar importer preserves these lines, including author order, personal-name emphasis, and contribution markers. Update the override together with the corresponding publication if its author list changes.
