==================
Environments
==================

When deploying to multiple environments (development, staging, production, etc.), you'll likely want to deploy different configurations. Each environment/configuration should have its own file in ``{{ project_name }}/settings`` and inherit from ``{{ project_name }}.settings.base``. A ``dev`` environment is provided as an example.

By default, ``manage.py`` and ``wsgi.py`` will use ``{{ project_name }}.settings.local`` if no settings module has been defined. To override this, use the standard Django constructs (setting the ``DJANGO_SETTINGS_MODULE`` environment variable or passing in ``--settings={{ project_name }}.settings.<env>``). Alternatively, you can symlink your environment's settings to ``{{ project_name }}/settings/local.py``.

You may want to have different ``wsgi.py`` and ``urls.py`` files for different environments as well. If so, simply follow the directory structure laid out by ``{{ project_name }}/settings``, for example::

    wsgi/
      __init__.py
      base.py
      dev.py
      ...

The settings files have examples of how to point Django to these specific environments.