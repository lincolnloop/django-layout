import contextlib
import re

# Django's lexer stops a block tag at a newline; DOTALL lets long tags wrap.
# Native in Django 6.2; drop this patch on upgrade.
# https://forum.djangoproject.com/t/allow-newlines-inside-tags/36040/37
# https://github.com/django/django/pull/21982
# Django is absent when the cog pre-commit hook imports project_name.config.
with contextlib.suppress(ModuleNotFoundError):
    from django.template import base

    base.tag_re = re.compile(base.tag_re.pattern, base.tag_re.flags | re.DOTALL)
