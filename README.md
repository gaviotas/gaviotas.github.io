# Minhyun Lee Website

Personal academic website built with Quarto and deployed to GitHub Pages or Netlify.

## Stack

- Quarto website
- Custom SCSS theme in `styles.scss`
- Static PDF resume in `static/uploads/resume.pdf`
- Publication import helper in `scripts/import_scholar.py`

## Project Structure

```text
.
├── .github/workflows/publish.yaml   # GitHub Pages deployment
├── _quarto.yml                      # Site config and navigation
├── assets/
│   └── profile/portrait.jpeg        # Homepage hero image
├── data/
│   └── publications.json            # Cached publication data
├── index.qmd                        # Homepage
├── netlify.toml                     # Netlify build config
├── pages/
│   ├── cv.qmd
│   ├── publications.qmd
│   └── research.qmd
├── scripts/
│   └── import_scholar.py            # Google Scholar importer
├── static/
│   └── uploads/resume.pdf
└── styles.scss
```

## Local Development

Quarto CLI is required.

```bash
quarto preview
```

To generate the static site once:

```bash
quarto render
```

The output is written to `_site/`.

## Publications Update

The publication page is generated from the public Google Scholar profile configured in `scripts/import_scholar.py`.

```bash
python3 scripts/import_scholar.py
```

This updates:

- `data/publications.json`
- `pages/publications.qmd`

## Deployment

- GitHub Pages: `.github/workflows/publish.yaml`
- Netlify: `netlify.toml`

Both deployment targets now render the site with Quarto instead of the previous Hugo-based template pipeline.
