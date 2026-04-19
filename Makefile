JEKYLL := ./scripts/jekyll-local
PORT ?= 4000

.PHONY: setup install render preview

setup:
	./scripts/setup-jekyll-local.sh

install: setup

render: install
	$(JEKYLL) jekyll build

preview: install
	$(JEKYLL) jekyll serve --host 0.0.0.0 --port $(PORT)
