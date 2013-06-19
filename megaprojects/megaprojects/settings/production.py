"""Production settings and globals."""


from os import environ

from base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

INSTALLED_APPS += ('gunicorn',)

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_setting('DATABASE_NAME'),
        'USER': get_env_setting('DATABASE_USER'),
        'PASSWORD': get_env_setting('DATABASE_PASS'),
        'HOST': get_env_setting('DATABASE_HOST'),
        'PORT': get_env_setting('DATABASE_PORT'),
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': get_env_setting('CACHE_LOCATION'),
    }
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#cache-middleware-anonymous-only
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION


########## SECURITY CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = get_env_setting('ALLOWED_HOSTS')
########## END SECURITY CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = get_env_setting('STATIC_ROOT')
########## END STATIC FILE CONFIGURATION


########## DJANGO ANALYTICAL CONFIGURATION
# See: http://pythonhosted.org/django-analytical/features.html#identifying-visitors
ANALYTICAL_AUTO_IDENTIFY = get_env_setting('ANALYTICAL_AUTO_IDENTIFY')

# See: http://pythonhosted.org/django-analytical/services/google_analytics.html#setting-the-property-id
GOOGLE_ANALYTICS_PROPERTY_ID = get_env_setting('GOOGLE_ANALYTICS_PROPERTY_ID')

# See: http://pythonhosted.org/django-analytical/services/google_analytics.html#tracking-multiple-domains
GOOGLE_ANALYTICS_TRACKING_STYLE = get_env_setting('GOOGLE_ANALYTICS_TRACKING_STYLE')
########## END DJANGO ANALYTICAL CONFIGURATION


########## ADDTHIS CONFIGURATION
ADDTHIS_PUB_ID = get_env_setting('ADDTHIS_PUB_ID')

ADDTHIS_GA_TRACKING_ENABLED = get_env_setting('ADDTHIS_GA_TRACKING_ENABLED')
########## END ADDTHIS CONFIGURATION


########## INTENSEDEBATE CONFIGURATION
INTENSEDEBATE_ACCT = get_env_setting('INTENSEDEBATE_ACCT')
########## END INTENSEDEBATE CONFIGURATION
