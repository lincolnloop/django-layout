{% comment %}

# Django Layout

`django-layout` provides sane defaults for new Django projects based on
[established best
practices](http://lincolnloop.com/django-best-practices/) and some
configuration setups frequently used in Lincoln Loop\'s projects, like
[using pip-tools for dependency
locking](https://lincolnloop.com/blog/python-dependency-locking-pip-tools/),
[using
setup.py](https://lincolnloop.com/blog/using-setuppy-your-django-project/)
and [making manage.py a console
script](https://lincolnloop.com/blog/goodbye-managepy/).

To use `django-layout`:

1.  follow the steps for Python installation from the
    [Pre-Requisites](#pre-requisites) section;

2.  create and activate a virtualenv:

        python3.9 -m venv .venv
        . .venv/bin/activate

3.  install Django with `pip install django` or
    `pip install Django==3.2b1` if you want the latest version;

4.  run the following command:

        django-admin.py startproject --template=https://github.com/lincolnloop/django-layout/zipball/main --extension=py,md,gitignore,cfg,in,yml,json,dockerignore --name=Makefile,Dockerfile {{ project_name }}

## Postgres

If you want to use Postgres database, you can

-   go to the generated project folder,

-   uncomment the lines preceded by `# Postgres` in

    -   `requirements/requirements.in`
    -   `docker-compose.yml`
    -   `{{ project_name }}/config.py`

-   replace `{{ project_name }}` with the project name you chose.

Another alternative is to

-   download this repository to your local machine,

-   uncomment the lines preceded by `# Postgres` in

    -   `requirements/requirements.in`
    -   `docker-compose.yml`
    -   `{{ project_name }}/config.py`

-   run the command with the appropriate path to the `django-layout`
    folder:

```
        django-admin.py startproject --template=<PATH_TO>/django-layout --extension=py,md,gitignore,cfg,in,yml,json,dockerignore --name=Makefile,Dockerfile {{ project_name }}
```

Note

The text following this comment block will become the README.md of the new project.

------------------------------------------------------------------------

{% endcomment %}

# {{ project_name }}

## Docker Installation

Build and run the project:

    docker-compose build
    docker-compose up

To run Django commands like migrations and shell or to enter the
container bash do:

    docker-compose run --rm app bash
    docker-compose run --rm app manage.py createsuperuser
    docker-compose run --rm app manage.py migrate
    docker-compose run --rm app manage.py shell

To stop containers run:

    docker-compose down

To update a container after adding a new requirement for example:

    docker-compose build app
    docker-compose build client

## Local Installation

### Pre-Requisites

**Python3.9**

To install all of the system dependencies on a Debian-based system, run:

    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.9 python3.9-venv python3.9-dev

### Creating the Virtual Environment

First, create a clean base environment using virtualenv:

    make .venv/bin/activate
    . .venv/bin/activate

### Installing the Project

Compile requirements to make sure you have all the latest dependencies:

    make upgrade-pip
    make requirements.txt
    make requirements/dev.txt

Install the requirements and the project source:

    make install
    make install-dev

### Configuring a Local Environment

If you\'re just checking the project out locally, you can generate the
configuration file with already filled default values:

    make {{ project_name }}.yml

This will create the `{{ project_name }}.yml` file where you can
customize the variables used in project settings.

### Optional: Configuring Postgres

If you want to use Postgres for the database, install it according to
your OS requirements.

To configure the database enter PSQL shell and create the database and
user:

    $ sudo -u postgres psql
    postgres=# create database {{ project_name }};
    postgres=# create user {{ project_name }};
    postgres=# alter role dataplatform SUPERUSER;
    postgres=# alter role dataplatform with password '{{ project_name }}';

Replace `{{ project_name }}` with whatever values you want for database,
user and password.

Change the value of `DATABASE_URL` in `{{ project_name }}.yml`:

    DATABASE_URL: postgres://{{ project_name }}:{{ project_name }}@localhost:5432/{{ project_name }}

Replace the appropriate credentials if necessary.

## Running the project

### Docker

Run migrations:

    docker-compose run --rm app manage.py migrate

Create super user:

    docker-compose run --rm app manage.py createsuperuser

Make sure you have the containers running:

    docker-compose up

Access [localhost:8000/admin](localhost:8000/admin).

### Local

Run migrations:

    manage.py migrate

Create super user:

    manage.py createsuperuser

Run the server:

    manage.py runserver

Access [localhost:8000/admin](localhost:8000/admin).
