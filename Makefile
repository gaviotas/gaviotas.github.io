PORT ?= 4000

.PHONY: setup build serve preview
setup:
	npm ci
build:
	npm run build
serve:
	npm run dev -- --port $(PORT)
preview:
	npm run preview -- --port $(PORT)
