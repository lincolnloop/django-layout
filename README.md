{% comment %}

# Django Layout

`django-layout` provides sane defaults for new Django projects based on
[established best
practices](http://lincolnloop.com/django-best-practices/) and some
configuration setups frequently used in Lincoln Loop\'s projects, like
[using `pip-tools` for dependency
locking](https://lincolnloop.com/blog/python-dependency-locking-pip-tools/),
[using
`pyproject.toml`](https://lincolnloop.com/insights/using-pyprojecttoml-in-your-django-project/).

To use `django-layout`:

1. create and activate a virtualenv:

        python -m venv --prompt . --upgrade-deps .venv

2. install Django with `pip install django`

3. run the following command (replace `YOUR_PROJECT_NAME` with your preferred name):

        django-admin startproject \
         --template=https://github.com/lincolnloop/django-layout/zipball/main \
         --extension=py,md,gitignore,yml,json \
         --name=Makefile,Dockerfile \
         --exclude=.github \
         YOUR_PROJECT_NAME

*Note:  The text following this comment block will become the README.md of the new project.*

------------------------------------------------------------------------

{% endcomment %}

# {{ project_name }}

## Docker Installation

Build and run the project:

    docker compose up --build

To run Django commands like migrations and shell or to enter the
container bash do:

    docker compose run --rm app bash
    docker compose run --rm app manage.py createsuperuser
    docker compose run --rm app manage.py migrate
    docker compose run --rm app manage.py shell

To stop containers run:

    docker compose down

To update a container after adding a new requirement for example:

    docker compose build

## Running the project

### Docker

Create super user:

    docker compose run --rm app manage.py createsuperuser

Make sure you have the containers running:

    docker compose up

Access [localhost:8000/{{ project_name }}/admin/](http://localhost:8000/{{ project_name }}/admin/).

## Configuration / Environment Variables

<!-- [[[cog
import cog
from {{ project_name }}.config import Config
mdown = Config.generate_markdown()
cog.out('\n'.join(mdown.split('\n')[1:]))
]]] -->

* **DEBUG**
  * type: `bool`
  * default: `False`
* **ALLOWED_HOSTS**
  * description: Hosts allowed to serve the site https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts
  * type: `list[str]`
  * default: `['*']`
* **DATABASE_URL**
  * description: A string with the database URL as defined in https://github.com/jacobian/dj-database-url#url-schema
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
  * description: A long random string you keep secret https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key
  * type: `str`
* **ENVIRONMENT**
  * description: Deploy environment
  * type: `str`
  * default: `test`
* **BASIC_AUTH_CREDENTIALS**
  * description: Basic Auth credentials for the site in the format 'username:password'
  * type: `str`
  * default: ``
<!-- [[[end]]] -->

## Makefile commands

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

README.md                 Update dynamic blocks in README.md
fix                       Fix linting errors
fmt                       Format Python code
lint                      Lint Python code
requirements.txt          Generate requirements.txt (and requirements-dev.txt) from pyproject.toml
test                      Run tests
upgrade-requirements      Upgrade all dependencies in requirements.txt and requirements-dev.txt
```
<!-- [[[end]]] -->
