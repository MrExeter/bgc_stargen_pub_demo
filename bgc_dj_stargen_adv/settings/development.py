from .base import *
from settings_secret import *
import os

DEBUG = True

SECRET_KEY = "lkcoirkglpds0eolkflvf566454agflskdjflskdjfoawisjalskdjl;kjw45kmsgdfmks'kg"

# MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')
# MEDIA_URL = '/assets/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'bagc_test',
#         'USER': 'bgp_user',
#         'PASSWORD': '2Kz2vHDT4Lprczp98X28RG9jx7LYP7vp',
#         'HOST': '127.0.0.1',
#         'PORT': 5432,
#     }
# }

# For Development ONLY!   run   python -m smtpd -n -c DebuggingServer localhost:1025 in separate terminal
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'No Reply <noreply@jtsinteractive.com>'


DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

print("Static Files Dirs = {}".format(STATICFILES_DIRS))
print("Static Root".format(STATIC_ROOT))
