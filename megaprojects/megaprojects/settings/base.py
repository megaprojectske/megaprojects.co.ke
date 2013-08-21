"""Common settings and globals."""


from os.path import abspath, basename, dirname, join, normpath
from sys import path


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: http://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)

# See: http://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Africa/Nairobi'

# See: http://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: http://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: http://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: http://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: http://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: http://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: http://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: http://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: http://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = r"+rk7txvm*l^3n9c-=#9je1qzi0xvq!^#1f&we2u463%pa63hvm"
########## END SECRET CONFIGURATION


########## FIXTURE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION

########## TEMPLATE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: http://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: http://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'core.middleware.MinifyHTMLMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    # 'django.contrib.humanize',
)

THIRD_PARTY_APPS = (
    'addthis',
    'bootstrap-pagination',
    'ckeditor',
    'ganalytics',
    'haystack',
    'intensedebate',
    'sorl.thumbnail',
    'south',
    'storages'
)

LOCAL_APPS = (
    'articles',
    'blog',
    'core',
    'menu',
    'programs',
)

# See: http://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: http://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION


########## CKEDITOR CONFIGURATION
# See: http://github.com/shaunsephton/django-ckeditor#required
CKEDITOR_UPLOAD_PATH = normpath(join(SITE_ROOT, 'ckeditor'))

# See: http://github.com/shaunsephton/django-ckeditor#optional
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Full': [
            ['Source', '-', 'Save', 'NewPage', 'DocProps', 'Preview', 'Print'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'SpellChecker', 'Scayt'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'],
            ['Link', 'Unlink', 'Anchor'],
            ['Table', 'HorizontalRule', 'SpecialChar'],
            ['Format'],
            ['Maximize', 'ShowBlocks', '-', 'About'],
        ],
        'forcePasteAsPlainText': True,
        'scayt_autoStartup': True,
        'scayt_sLang': 'en_GB',
        'startupOutlineBlocks': True,
    },
}
########## END CKEDITOR CONFIGURATION


########## HAYSTACK CONFIGURATION
# See: http://django-haystack.readthedocs.org/en/latest/tutorial.html#configuration
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': normpath(join(SITE_ROOT, 'whoosh_index')),
    },
}
########## END HAYSTACK CONFIGURATION


########## THUMBNAIL CONFIGURATION
# See: http://sorl-thumbnail.readthedocs.org/en/latest/reference/settings.html#thumbnail-progressive
THUMBNAIL_PROGRESSIVE = False

# See: http://sorl-thumbnail.readthedocs.org/en/latest/reference/settings.html#thumbnail-upscale
THUMBNAIL_UPSCALE = False

# See: http://sorl-thumbnail.readthedocs.org/en/latest/reference/settings.html#thumbnail-format
THUMBNAIL_FORMAT = 'PNG'
########## THUMBNAIL CONFIGURATION
