#!/bin/bash
# Intended to run in a docker container. Called by `make requirements.txt`
set -euf -o pipefail

pip install --disable-pip-version-check --root-user-action=ignore -U pip pip-tools
# Compile main requirements
pip-compile -v \
  --resolver=backtracking \
  --generate-hashes \
  --strip-extras \
  --output-file=requirements.txt \
  pyproject.toml

# Compile dev requirements
pip-compile -v \
  --constraint $(pwd)/requirements.txt \
  --resolver=backtracking \
  --generate-hashes \
  --extra=dev \
  --output-file=requirements-dev.txt \
  pyproject.toml
