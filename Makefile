#
# See `make help` for a list of all available commands.

SHELL=/bin/bash -eu -o pipefail

.PHONY: upgrade-requirements
upgrade-requirements:  ## Upgrade all dependencies in uv.lock
	uv lock --upgrade

README.md: {{ project_name }}/config.py Makefile ## Update dynamic blocks in README.md
	cog -r README.md

.PHONY: fmt
fmt:  ## Format Python code
	ruff format .

.PHONY: lint
lint:  ## Lint Python code
	ruff check .

.PHONY: fix
fix:  ## Fix linting errors
	ruff check --fix .

.PHONY: test
test:  ## Run tests
	python manage.py test --parallel

.PHONY: help
help:
	@echo -e "Available make commands:"
	@echo -e ""
	@echo "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sort | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\1:\2/' | awk -F: '{ printf "%-25s %s\n", $$1, $$2 }')"

.DEFAULT_GOAL := help
