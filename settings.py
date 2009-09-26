# Django settings for website project.

import sys
import os

PROJECT_ROOT = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'compat'))

DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
DISABLE_TRANSACTION_MANAGEMENT = True

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'mytask.db'     # Or path to database file if using sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Kiev'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

ADMIN_MEDIA_PREFIX = '/amedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!v=qx9a0&04(c=c=+l$6n!ya)g20rp7%um!5qtcp3^3xg(-o^g'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'
LOGIN_URL = '/login/'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT, 'template')
)

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)

FIXTURE_DIRS = (
	PROJECT_ROOT + '/apps/userdata/fixtures',
)

INSTALLED_APPS = (
    'django.contrib.auth',
	'django.contrib.sessions',
    'django.contrib.contenttypes',
	'userdata',
)