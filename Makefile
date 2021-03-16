#
# See `make help` for a list of all available commands.

SHELL=/bin/bash -eu -o pipefail

.venv/bin/activate:
	python3.9 -m venv --prompt $(shell basename $(shell pwd)) .venv

.PHONY: install
install: .venv/bin/activate  # Install Python dependencies
	./.venv/bin/pip install -r requirements.txt
	./.venv/bin/pip install -e .

.PHONY: install-dev
install-dev: .venv/bin/activate  # Install Python dependencies
	./.venv/bin/pip install -r requirements/dev.txt
	./.venv/bin/pip install -e .

upgrade-pip:
	pip install --upgrade pip wheel setuptools pip-tools

requirements.txt: requirements/requirements.in
	pip-compile --generate-hashes --output-file=$@ requirements/requirements.in

requirements/dev.txt: requirements/dev.in requirements.txt
	pip-compile --generate-hashes --output-file=$@ requirements/dev.in

{{ project_name }}.yml:
	./.venv/bin/generate-config > $@

.PHONY: fmt
fmt:
	isort .
	black .

.PHONY: help
help:
	@echo -e "Available make commands:"
	@echo -e ""
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sort | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

.DEFAULT_GOAL := help
