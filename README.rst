{% comment %}

===============
Django Layout
===============

``django-layout`` provides sane defaults for new Django projects based on `established best practices <http://lincolnloop.com/django-best-practices/>`__.

To use ``django-layout``:

1. follow the steps for Python instalation from the `Pre-Requisites`_ section;
2. create and activate a virtualenv::

    python3.9 -m venv .venv
    . .venv/bin/activate

3. install Django with :code:`pip install django` or :code:`pip install Django==3.2b1` if you want the latest version;
4. run the following command::

     django-admin.py startproject --template=https://github.com/lincolnloop/django-layout/zipball/master --extension=py,rst,gitignore,cfg,in --name=Makefile {{ project_name }}

.. note:: The text following this comment block will become the README.rst of the new project.

-----

{% endcomment %}

======================
{{ project_name }}
======================

Installation
============

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


Running the project
===================

Run migrations::

    manage.py migrate

Create super user::

    manage.py createsuperuser

Run the server::

    manage.py runserver

Access `localhost:8000/admin <localhost:8000/admin>`_.
