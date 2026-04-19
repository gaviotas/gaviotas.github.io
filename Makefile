QUARTO := ./scripts/quarto-local
PORT ?= 4173

.PHONY: quarto-check render preview

quarto-check:
	$(QUARTO) check

render:
	mkdir -p _site/pages
	$(QUARTO) render

preview:
	mkdir -p _site/pages
	$(QUARTO) render
	python3 -m http.server $(PORT) -d _site
