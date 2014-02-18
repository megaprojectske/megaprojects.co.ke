"""Development settings and globals."""


from os.path import join, normpath

from base import *


########## DEBUG CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: http://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: http://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)

# See: http://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: http://github.com/django-debug-toolbar/django-debug-toolbar#installation
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# See: http://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
########## END TOOLBAR CONFIGURATION


########## SORL THUMBNAIL CONFIGURATION
# See: http://sorl-thumbnail.readthedocs.org/en/latest/logging.html#errors-logging
THUMBNAIL_DEBUG = False
########## END SORL THUMBNAIL CONFIGURATION


GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-000000-1'
GOOGLE_ANALYTICS_SITE_DOMAIN = 'example.com'
GOOGLE_PLUS_PUBLISHER='000000000000000000001'

ADDTHIS_PUB_ID = 'ra-0000000000000000'
ADDTHIS_GA_TRACKING_ENABLED = False
ADDTHIS_TWITTER_BITLY=True
ADDTHIS_TWITTER_VIA='example'

INTENSEDEBATE_ACCT = '00000000000000000000000000000000'

ALLOWED_HOSTS = ['*']
