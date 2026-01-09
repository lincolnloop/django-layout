<!-- {% comment %} -->

<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." /></a>

# Django Layout

[![codecov](https://codecov.io/github/lincolnloop/django-layout/branch/main/graph/badge.svg?token=49GGtPkTeh)](https://codecov.io/github/lincolnloop/django-layout)

`django-layout` provides sane defaults for new Django projects based on established best
practices and some configuration setups frequently used in Lincoln Loop\'s projects. It
includes:

- `uv` for fast dependency management
- `ruff` for formatting and linting
- `goodconf` for structured & documented environment variable configuration
- structured logging in deployment and pretty logging in development
- `gunicorn` and `whitenoise` for production deployments
- production-hardened settings

## Usage

### With `uv`

Run the following command (replace `YOUR_PROJECT_NAME` with your preferred name):

        uv run --with django django-admin startproject \
         --template=https://github.com/lincolnloop/django-layout/zipball/main \
         --extension=py,md,gitignore,yaml,json,toml \
         --name=Makefile,Dockerfile \
         --exclude=.github \
         YOUR_PROJECT_NAME

### With `pip`

1.  create and activate a virtualenv:

        python -m venv --prompt . --upgrade-deps .venv

2.  install Django with `pip install django`

3.  run the following command (replace `YOUR_PROJECT_NAME` with your preferred name):

        django-admin startproject \
         --template=https://github.com/lincolnloop/django-layout/zipball/main \
         --extension=py,md,gitignore,yaml,json,toml \
         --name=Makefile,Dockerfile \
         --exclude=.github \
         YOUR_PROJECT_NAME

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on setting up the development
environment and testing the template.

This `README.md` file is kept up-to-date by pre-commit, and is run when composing a new
commit. To execute it manually, run:

```
pre-commit run cog
```

Then use `git add -p README.md` to only commit the changes you want. You can `git stash`
the template changes after your commit.

---

<details>
<summary>Click to preview the generated project README</summary>

<!-- {% endcomment %} -->

# {{ project_name }}

## Docker Installation

Build and run the project:

    make init
    docker compose up

To run Django commands like migrations and shell or to enter the container bash do:

    docker compose run --rm app bash
    docker compose run --rm app python manage.py createsuperuser
    docker compose run --rm app python manage.py migrate
    docker compose run --rm app python manage.py shell

To stop containers run:

    docker compose down

To update a container after adding a new requirement for example:

    docker compose build

## Running the project

### Docker

Create super user:

    docker compose run --rm app python manage.py createsuperuser

Make sure you have the containers running:

    docker compose up

Access http://localhost:8000/{{ project_name }}-admin/.

## Configuration / Environment Variables

<!-- prettier-ignore-start -->

<!-- [[[cog
import importlib
import cog

project_name = "{{ project_name }}"
if project_name.startswith("{{"):
    project_name = "project_name"

config_module = importlib.import_module(project_name + ".config")
config = config_module.Config
print(f"\nReading {config_module.__name__}.Config")
mdown = config_module.Config.generate_markdown()
cog.out('\n'.join(mdown.split('\n')[1:]))
]]] -->

* **DEBUG**
  * type: `bool`
  * default: `False`
* **ALLOWED_HOSTS**
  * description: Hosts allowed to serve the site https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#allowed-hosts
  * type: `list[str]`
  * default: `['*']`
* **DATABASE_URL**
  * description: A string with the database URL as defined in https://github.com/jazzband/dj-database-url#url-schema
  * type: `str`
  * default: `sqlite:///./sqlite3.db`
* **DJANGO_ENV**
  * description: Toggle deployment settings for local development or production
  * type: `Literal['development', 'dev', 'production']`
  * default: `production`
* **LOG_LEVEL**
  * description: Python logging level
  * type: `Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']`
  * default: `INFO`
* **SECRET_KEY** _REQUIRED_
  * description: A long random string you keep secret https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#secret-key
  * type: `str`
* **ENVIRONMENT**
  * description: Name of deployed environment (e.g. 'staging', 'production')
  * type: `str`
  * default: `development`
* **BASIC_AUTH_CREDENTIALS**
  * description: Basic Auth credentials for the site in the format 'username:password'
  * type: `str`
  * default: ``
* **SENTRY_DSN**
  * description: Sentry DSN to enable error logging
  * type: `str`
  * default: ``
* **SENTRY_TRACES_SAMPLE_RATE**
  * description: Sentry trace sample rate https://docs.sentry.io/product/sentry-basics/concepts/tracing/trace-view/
  * type: `float`
  * default: `0.25`
* **TEMPLATE_DEBUG**
  * description: Enable to measure template coverage
  * type: `bool`
  * default: `False`
      <!-- [[[end]]] -->

<!-- prettier-ignore-end -->

## Makefile commands

<!-- prettier-ignore-start -->

<!-- [[[cog
import cog
import subprocess
cog.out(
    "```shell\n" +
    subprocess.check_output(["make", "help"]).decode() +
    "```"
)
]]] -->
```shell
Available make commands:

init                      Initialize the project
run                       Run the project
test                      Run tests
upgrade-requirements      Upgrade all dependencies in uv.lock
```
<!-- [[[end]]] -->

<!-- prettier-ignore-end -->

<!-- {% comment %} -->
</details>
<!-- {% endcomment %} -->
