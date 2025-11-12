#
# See `make help` for a list of all available commands.

SHELL=/bin/bash -eu -o pipefail

.PHONY: init
init:  ## Initialize the project
	command -v uvx || curl -LsSf https://astral.sh/uv/install.sh | sh \
		&& docker compose build \
		&& docker compose run --rm app python manage.py migrate \
		&& git init && git add . \
		&& command -v pre-commit || uv tool install pre-commit \
		&& pre-commit install

.PHONY: run
run:  ## Run the project
	docker compose up

.PHONY: upgrade-requirements
upgrade-requirements:  ## Upgrade all dependencies in uv.lock
	uv lock --upgrade

.PHONY: test
test:  ## Run tests
	docker compose run --rm app pytest

.PHONY: help
help:
	@echo -e "Available make commands:"
	@echo -e ""
	@echo "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sort | sed -E 's/:.*##[[:space:]]*/:/' | awk -F: '{ printf "%-25s %s\n", $$1, $$2 }')"

.DEFAULT_GOAL := help
