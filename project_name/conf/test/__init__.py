from {{ project_name }}.settings import *   # pylint: disable=W0614,W0401

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
ROOT_URLCONF = '{{ project_name }}.conf.test.urls'

INSTALLED_APPS += (
    'django.contrib.admin'
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
