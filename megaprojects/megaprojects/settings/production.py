"""Production settings and globals."""


import ast
from os import environ

from base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """

    try:
        value = environ[setting]
        # Try convert values to their python objects
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


INSTALLED_APPS += ('gunicorn',)


########## FILE STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
########## END FILE STORAGE CONFIGURATION


########## COMMON MIDDLEWARE CONFIGURATION
# See: http://docs.djangoproject.com/en/1.5/ref/settings/#prepend-www
PREPEND_WWW = True
########## END COMMON MIDDLEWARE CONFIGURATION


########## EMAIL CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django_ses.SESBackend'

# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-host
# EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
# EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
# EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-port
# EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
# EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
# EMAIL_USE_TLS = True

# See: http://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = get_env_setting('SERVER_EMAIL')
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
# See: http://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': get_env_setting('CACHE_LOCATION'),
    }
}

# See: http://docs.djangoproject.com/en/dev/ref/settings/#cache-middleware-anonymous-only
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION


########## SECURITY CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = get_env_setting('ALLOWED_HOSTS')
########## END SECURITY CONFIGURATION


########## AWS CONFIGURATION
AWS_ACCESS_KEY_ID = get_env_setting('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = get_env_setting('AWS_SECRET_ACCESS_KEY')
########## AWS CONFIGURATION


########## STORAGES CONFIGURATION
AWS_STORAGE_BUCKET_NAME = get_env_setting('AWS_STORAGE_BUCKET_NAME')

# See: http://www.eliotk.net/05/30/force-http-with-django-storages-and-s3boto/
AWS_S3_SECURE_URLS = get_env_setting('AWS_S3_SECURE_URLS')

# See: django-storages (storages.backends.s3boto)
AWS_S3_CUSTOM_DOMAIN = get_env_setting('AWS_S3_CUSTOM_DOMAIN')

# See: django-storages (storages.backends.s3boto)
AWS_IS_GZIPPED = get_env_setting('AWS_IS_GZIPPED')

# See: http://docs.aws.amazon.com/AmazonS3/latest/dev/S3_QSAuth.html/
AWS_QUERYSTRING_AUTH = get_env_setting('AWS_QUERYSTRING_AUTH')
########## END STORAGES CONFIGURATION


########## S3 FOLDER STORAGE CONFIGURATION
# See: http://github.com/jamstooks/django-s3-folder-storage#configuration
DEFAULT_S3_PATH = get_env_setting('DEFAULT_S3_PATH')

# See: http://github.com/jamstooks/django-s3-folder-storage#configuration
STATIC_S3_PATH = get_env_setting('STATIC_S3_PATH')
########## END S3 FOLDER STORAGE CONFIGURATION


########## MEDIA CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = "/%s/" % DEFAULT_S3_PATH

# See: http://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "//%s/media/" % AWS_STORAGE_BUCKET_NAME
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = "/%s/" % STATIC_S3_PATH

# See: http://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "//%s/static/" % AWS_STORAGE_BUCKET_NAME
########## END STATIC FILE CONFIGURATION


########## GOOGLE_ANALYTICS CONFIGURATION
GOOGLE_ANALYTICS_PROPERTY_ID = get_env_setting('GOOGLE_ANALYTICS_PROPERTY_ID')

GOOGLE_ANALYTICS_SITE_DOMAIN = get_env_setting('GOOGLE_ANALYTICS_SITE_DOMAIN')

GOOGLE_PLUS_PUBLISHER = get_env_setting('GOOGLE_PLUS_PUBLISHER')
########## END GOOGLE_ANALYTICS CONFIGURATION


########## ADDTHIS CONFIGURATION
ADDTHIS_GA_TRACKING_ENABLED = get_env_setting('ADDTHIS_GA_TRACKING_ENABLED')

ADDTHIS_PUB_ID = get_env_setting('ADDTHIS_PUB_ID')

ADDTHIS_TWITTER_BITLY = get_env_setting('ADDTHIS_TWITTER_BITLY')

ADDTHIS_TWITTER_VIA = get_env_setting('ADDTHIS_TWITTER_VIA')
########## END ADDTHIS CONFIGURATION


########## INTENSEDEBATE CONFIGURATION
INTENSEDEBATE_ACCT = get_env_setting('INTENSEDEBATE_ACCT')
########## END INTENSEDEBATE CONFIGURATION
