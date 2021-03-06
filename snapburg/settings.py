"""
Django settings for snapburg project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import getpass
import json
import os

from common.base_dir import project_root_join

MAIN_URL = "http://osia.hipisi.org.pl"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'jquery',
    'bootstrap4',
    'rest_framework',
    'django_extensions',
    'drf_yasg',
    'qrcode',
    'imagekit',
    'webpack_loader',

    # 'taggit',
    # 'photologue',
    # 'sortedm2m',

    'apps.galleries',
    'apps.snaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'common.middleware.global_request_middleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

EMAIL_FROM = os.environ.get('EMAIL_FROM', 'notifications@hipisi.org.pl')
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 25))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS'))
EMAIL_USE_SSL = bool(os.environ.get('EMAIL_USE_SSL'))

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     os.environ.get('DATABASE_NAME', getpass.getuser()),
        'USER':     os.environ.get('DATABASE_USER', getpass.getuser()),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST':     os.environ.get('DATABASE_HOST', ''),
        'PORT':     os.environ.get('DATABASE_PORT', ''),
        'OPTIONS':  json.loads(os.environ.get('DATABASE_OPTIONS', '{}')),
    }
}

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = bool(os.environ.get('DEBUG'))

ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = [
    project_root_join("static"),
    project_root_join("dist"),
]

MEDIA_ROOT = project_root_join('media')
MEDIA_URL = '/media/'

SITE_ID = 1

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

ROOT_URLCONF = 'snapburg.urls'

TEMPLATES = [
    {
        'BACKEND':  'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS':     [
            project_root_join('templates'),
        ],
        'OPTIONS':  {
            'debug':              DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    }
]
WSGI_APPLICATION = 'snapburg.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'PAGE_SIZE':                20,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_SCHEMA_CLASS':     'rest_framework.schemas.coreapi.AutoSchema'
}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH':     False,
    'DOC_EXPANSION':        'list',
    'APIS_SORTER':          'alpha',
    'SECURITY_DEFINITIONS': None,
}

TAGGIT_CASE_INSENSITIVE = True

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE':      'webpack-stats.json',
    }
}

# Local settings environment, here simple as is possible
# in future should be based on environment variables

try:
    from _local_settings import *
except ImportError as e:
    pass
