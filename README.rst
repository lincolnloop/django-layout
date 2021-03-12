.. {% comment %}

===============
Django Layout
===============

``django-layout`` provides sane defaults for new Django projects based on `established best practices <http://lincolnloop.com/django-best-practices/>`__. To use ``django-layout`` run the following command::

     django-admin.py startproject --template=https://github.com/lincolnloop/django-layout/zipball/master --extension=py,rst,gitignore,example {{ project_name }}

.. note:: The text following this comment block will become the README.rst of the new project.

-----

.. {% endcomment %}

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


This will create the `{{ project_name }}.yml` file where you can customize the appropriate variables.
