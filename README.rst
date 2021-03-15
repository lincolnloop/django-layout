{% comment %}

===============
Django Layout
===============

``django-layout`` provides sane defaults for new Django projects based on 
`established best practices <http://lincolnloop.com/django-best-practices/>`__ and some configuration setups 
frequently used in Lincoln Loop's projects, like 
`using pip-tools for dependency locking <https://lincolnloop.com/blog/python-dependency-locking-pip-tools/>`__, 
`using setup.py <https://lincolnloop.com/blog/using-setuppy-your-django-project/>`__ and 
`making manage.py a console script <https://lincolnloop.com/blog/goodbye-managepy/>`__.


To use ``django-layout``:

1. follow the steps for Python instalation from the `Pre-Requisites`_ section;
2. create and activate a virtualenv::

    python3.9 -m venv .venv
    . .venv/bin/activate

3. install Django with :code:`pip install django` or :code:`pip install Django==3.2b1` if you want the latest version;
4. run the following command::

     django-admin.py startproject --template=https://github.com/lincolnloop/django-layout/zipball/master --extension=py,rst,gitignore,cfg,in,yml,json,dockerignore --name=Makefile,Dockerfile {{ project_name }}


Postgres
========

If you want to use Postgres database, you can

- go to the generated project folder,
- uncomment the lines preceded by :code:`# Postgres` in
    - :code:`requirements/requirements.in`
    - :code:`docker-compose.yml`
    - :code:`{{ project_name }}/config.py`
- replace :code:`{{ project_name }}` with the project name you chose.

Another alternative is to

- download this repository to your local machine,
- uncomment the lines preceded by :code:`# Postgres` in
    - :code:`requirements/requirements.in`
    - :code:`docker-compose.yml`
    - :code:`{{ project_name }}/config.py`
- run the command with the appropriate path to the :code:`django-layout` folder::

     django-admin.py startproject --template=<PATH_TO>/django-layout --extension=py,rst,gitignore,cfg,in,yml,json,dockerignore --name=Makefile,Dockerfile {{ project_name }}

.. note:: The text following this comment block will become the README.rst of the new project.

-----

{% endcomment %}

======================
{{ project_name }}
======================

Docker Installation
===================

Build and run the project::

    docker-compose build
    docker-compose up

To run Django commands like migrations and shell or to enter the container bash do::

    docker-compose run --rm app bash
    docker-compose run --rm app manage.py createsuperuser
    docker-compose run --rm app manage.py migrate
    docker-compose run --rm app manage.py shell

Local Installation
==================

Pre-Requisites
--------------

**Python3.9**

To install all of the system dependencies on a Debian-based system, run::

    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.9 python3.9-venv python3.9-dev

Creating the Virtual Environment
--------------------------------

First, create a clean base environment using virtualenv::

    make .venv/bin/activate
    . .venv/bin/activate


Installing the Project
----------------------

Compile requirements to make sure you have all the latests dependencies::

    make upgrade-pip
    make requirements.txt
    make requirements/dev.txt


Install the requirements and the project source::

    make install


Configuring a Local Environment
-------------------------------

If you're just checking the project out locally, you can generate the configuration file with already filled default values::

    make {{ project_name }}.yml


This will create the :code:`{{ project_name }}.yml` file where you can customize the variables used in project settings.

Optional: Configuring Postgres
------------------------------

If you want to use Postgres for the database, install it according to your OS requirements.

To configure the database enter PSQL shell and create the database and user::

    $ sudo -u postgres psql
    postgres=# create database {{ project_name }};
    postgres=# create user {{ project_name }};
    postgres=# alter role dataplatform SUPERUSER;
    postgres=# alter role dataplatform with password '{{ project_name }}';

Replace :code:`{{ project_name }}` with whatever values you want for database, user and password.

Change the value of :code:`DATABASE_URL` in :code:`{{ project_name }}.yml`::

    DATABASE_URL: postgres://{{ project_name }}:{{ project_name }}@localhost:5432/{{ project_name }}

Replace the appropriate credentials if necessary.

Running the project
===================

Local
-----

Run migrations::

    manage.py migrate

Create super user::

    manage.py createsuperuser

Run the server::

    manage.py runserver

Access `localhost:8000/admin <localhost:8000/admin>`_.
