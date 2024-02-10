#
# See `make help` for a list of all available commands.

SHELL=/bin/bash -eu -o pipefail

requirements.txt: pyproject.toml  # Generate requirements.txt (and requirements-dev.txt) from pyproject.toml
	./bin/lock-requirements.sh

.PHONY: upgrade-requirements
upgrade-requirements:  # Upgrade all requirements to the latest version
	./bin/lock-requirements.sh --upgrade

{{ project_name }}.yml:
	./.venv/bin/generate-config > $@



.PHONY: fmt
fmt:  # Format Python code
	ruff format .

.PHONY: lint
lint:  # Lint Python code
	ruff check .

.PHONY: fix
fix:  # Fix linting errors
	ruff check --fix .

.PHONY: test
test:  # Run tests
	python manage.py test --parallel

.PHONY: help
help:
	@echo -e "Available make commands:"
	@echo -e ""
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sort | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

.DEFAULT_GOAL := help
