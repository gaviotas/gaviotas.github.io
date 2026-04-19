# Minhyun Lee Website

Personal academic website rebuilt on top of the original `msaveski/www_personal` Jekyll template.

## Stack

- Jekyll
- Skeleton CSS + template custom styles
- Data-driven content in `_data/`
- Google Scholar import helper in `scripts/import_scholar.py`
- Local Ruby/Jekyll bootstrap in `scripts/setup-jekyll-local.sh`

## Project Structure

```text
.
├── .github/workflows/publish.yaml
├── _config.yml
├── _data/
│   ├── experience.yaml
│   ├── main_info.yaml
│   └── publications.yaml
├── _includes/
├── _layouts/
├── assets/
│   ├── cv/cv_web.pdf
│   └── profile/portrait.jpeg
├── index.html
├── libs/
├── scripts/
│   └── import_scholar.py
└── Gemfile
```

## Local Development

Bootstrap local Ruby and install dependencies:

```bash
make setup
make install
```

Preview locally:

```bash
make preview
```

Build static output:

```bash
make render
```

The generated site is written to `_site/`.

The local runtime is installed under `.tools/` and does not require a system-wide Ruby installation.

## Publications Update

Refresh publications from Google Scholar:

```bash
python3 scripts/import_scholar.py
```

This updates `_data/publications.yaml`.

## Deployment

GitHub Pages deployment is handled in `.github/workflows/publish.yaml`.
