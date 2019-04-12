import whitenoise

from .base import *
import os
import dj_database_url
from decouple import config

import django_heroku

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Extra Security settings
#
# Enforce Https:
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
os.environ['HTTPS'] = "on"
os.environ['wsgi.url_scheme'] = 'https'

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SECURE_HSTS_PRELOAD = True

# Default to 60 minutes
SECURE_HSTS_SECONDS = 3600

ALLOWED_HOSTS = ['localhost',
                 'stargen-adv.herokuapp.com',
                 '*']
# COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


ManifestStaticFilesStorage.manifest_strict = False


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')
# MEDIA_URL = '/assets/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Application definition

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# DB settings
DATABASE_URL = config('DATABASE_URL')
DB_NAME = config('DB_NAME')
DB_PASS = config('DB_PASS')
DB_PORT = config('DB_PORT')
DB_USER = config('DB_USER')

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

DEBUG_PROPAGATE_EXCEPTIONS = True

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init("https://a8a43f925b4a4b05905d98043a8ae277@sentry.io/1361569")

django_heroku.settings(locals())
