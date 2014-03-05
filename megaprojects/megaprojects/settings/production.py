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


########## MANAGER CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    (get_env_setting('DJ_ADMIN_NAME'), get_env_setting('DJ_ADMIN_EMAIL')),
)

# See: http://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## FILE STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
########## END FILE STORAGE CONFIGURATION


########## EMAIL CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-host
# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-port
# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
from sendgridify import sendgridify
EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS = sendgridify()

# See: http://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: http://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = get_env_setting('DJ_SERVER_EMAIL')
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#databases
from postgresify import postgresify
DATABASES = postgresify()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#caches
from memcacheify import memcacheify
CACHES = memcacheify()

# See: http://docs.djangoproject.com/en/dev/ref/settings/#cache-middleware-anonymous-only
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('DJ_SECRET_KEY')
########## END SECRET CONFIGURATION


########## SECURITY CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = get_env_setting('DJ_ALLOWED_HOSTS')
########## END SECURITY CONFIGURATION


########## AWS CONFIGURATION
AWS_ACCESS_KEY_ID = get_env_setting('DJ_AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = get_env_setting('DJ_AWS_SECRET_ACCESS_KEY')
########## AWS CONFIGURATION


########## STORAGES CONFIGURATION
AWS_STORAGE_BUCKET_NAME = get_env_setting('DJ_AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = get_env_setting('DJ_AWS_S3_CUSTOM_DOMAIN')

# See: http://www.eliotk.net/05/30/force-http-with-django-storages-and-s3boto/
AWS_S3_SECURE_URLS = get_env_setting('DJ_AWS_S3_SECURE_URLS')

AWS_IS_GZIPPED = get_env_setting('DJ_AWS_IS_GZIPPED')

AWS_QUERYSTRING_AUTH = get_env_setting('DJ_AWS_QUERYSTRING_AUTH')
########## END STORAGES CONFIGURATION


########## S3 FOLDER STORAGE CONFIGURATION
# See: http://github.com/jamstooks/django-s3-folder-storage#configuration
DEFAULT_S3_PATH = get_env_setting('DJ_DEFAULT_S3_PATH')
########## END S3 FOLDER STORAGE CONFIGURATION


########## MEDIA CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = "/%s/" % DEFAULT_S3_PATH

# See: http://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "//%s/media/" % AWS_STORAGE_BUCKET_NAME
########## END MEDIA CONFIGURATION


########## GOOGLE_ANALYTICS CONFIGURATION
GOOGLE_ANALYTICS_PROPERTY_ID = get_env_setting('DJ_GOOGLE_ANALYTICS_PROPERTY_ID')

GOOGLE_ANALYTICS_SITE_DOMAIN = get_env_setting('DJ_GOOGLE_ANALYTICS_SITE_DOMAIN')

GOOGLE_PLUS_PUBLISHER = get_env_setting('DJ_GOOGLE_PLUS_PUBLISHER')
########## END GOOGLE_ANALYTICS CONFIGURATION


########## ADDTHIS CONFIGURATION
ADDTHIS_GA_TRACKING_ENABLED = get_env_setting('DJ_ADDTHIS_GA_TRACKING_ENABLED')

ADDTHIS_PUB_ID = get_env_setting('DJ_ADDTHIS_PUB_ID')

ADDTHIS_TWITTER_BITLY = get_env_setting('DJ_ADDTHIS_TWITTER_BITLY')

ADDTHIS_TWITTER_VIA = get_env_setting('DJ_ADDTHIS_TWITTER_VIA')
########## END ADDTHIS CONFIGURATION


########## INTENSEDEBATE CONFIGURATION
INTENSEDEBATE_ACCT = get_env_setting('DJ_INTENSEDEBATE_ACCT')
########## END INTENSEDEBATE CONFIGURATION
