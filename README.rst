{{ project_name }}
==================

Quickstart
----------

To bootstrap the project::

    virtualenv {{ project_name }}
    cd {{ project_name }}
    cd path/to/your/{{ project_name }}/repository
    pip install -r requirements.pip
    pip install -e .
    cp {{ project_name }}/settings/local.py.example {{ project_name }}/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
