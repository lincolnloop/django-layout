#!/bin/bash
# Intended to run in a docker container. Called by `make requirements.txt`
set -euf -o pipefail

# Check if --upgrade flag is provided
UPGRADE_FLAG=""
for arg in "$@"; do
  if [[ $arg == "--upgrade" ]]; then
    UPGRADE_FLAG="--upgrade"
  fi
done

# Compile main requirements
pip-compile $UPGRADE_FLAG -v \
  --resolver=backtracking \
  --generate-hashes \
  --strip-extras \
  --output-file=requirements.txt \
  pyproject.toml

# Compile dev requirements
pip-compile $UPGRADE_FLAG -v \
  --constraint "$(pwd)/requirements.txt" \
  --resolver=backtracking \
  --generate-hashes \
  --extra=dev \
  --output-file=requirements-dev.txt \
  pyproject.toml
