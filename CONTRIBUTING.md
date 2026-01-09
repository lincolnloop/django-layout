# Contributing

This repository is a Django project template. It uses `{{ project_name }}` placeholders
that get replaced when users run `django-admin startproject --template`.

To develop and test the template directly, we need to configure the environment so
Django can resolve these placeholders at runtime.

## Prerequisites

- Docker and Docker Compose

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/lincolnloop/django-layout.git
   cd django-layout
   ```

2. Set the `PROJECT_NAME` environment variable:

   ```bash
   export PROJECT_NAME=project_name
   ```

   Optionally, use [direnv](https://direnv.net/) to set this automatically:

   ```bash
   echo 'export PROJECT_NAME=project_name' > .envrc
   direnv allow
   ```

3. Build the project:

   ```bash
   make init
   ```

4. Run the tests:

   ```bash
   docker compose run --rm app pytest -n auto
   ```

5. Start the containers:

   ```bash
   docker compose up
   ```

6. Open http://localhost:8000 in your browser.

## Pre-commit Hooks

This project uses pre-commit for linting and formatting. Hooks run automatically on
commit, or manually with:

```bash
uv run pre-commit run --all-files
```

## Testing the Template

After making changes, verify the template still works:

```bash
mkdir /tmp/test-template && cd /tmp/test-template
uv run --with django django-admin startproject \
  --template=/path/to/django-layout \
  --extension=py,md,gitignore,yaml,json,toml \
  --name=Makefile,Dockerfile \
  --exclude=.venv \
  myproject .
```

Then follow the generated README to verify the new project runs correctly.
