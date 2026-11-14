import re

from django.template import base

# Django's lexer stops a {% %} tag at a newline; DOTALL lets long tags wrap.
# Native in Django 6.2; drop this patch on upgrade.
# https://forum.djangoproject.com/t/allow-newlines-inside-tags/36040/37
# https://github.com/django/django/pull/21982
base.tag_re = re.compile(base.tag_re.pattern, base.tag_re.flags | re.DOTALL)
