from {{ project_name }}.settings import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }
}

ROOT_URLCONF = '{{ project_name }}.conf.local.urls'

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
