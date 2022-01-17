# -*- coding: utf-8 -*-

__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

import os
from pathlib import Path
from loguru import logger
from decouple import config # noqa

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = BASE_DIR

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    # 'django_rq',

    'core.apps.CoreConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'core.middleware.CustomRemoteUserMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'core.middleware.CustomRemoteUserBackend',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
LOGS_ROOT = BASE_DIR / 'logs'

if not DEBUG:
    STATIC_ROOT = ROOT_DIR / 'nginx/static'
    MEDIA_ROOT = ROOT_DIR / 'nginx/media'
    LOGS_ROOT = ROOT_DIR / 'logs'

STATICFILES_DIRS = [APPS_DIR / 'config/static', ]

STATICFILES_FINDERS = [
  # First add the two default Finders, since this will overwrite the default.
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

DEFAULT_RENDERER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
)

if DEBUG:
    DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + (
        'rest_framework.renderers.BrowsableAPIRenderer',
    )

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES
}

X_FRAME_OPTIONS = 'SAMEORIGIN'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

EMAIL_HOST = config('SMTP_SRV')
EMAIL_PORT = 25
EMAIL_TIMEOUT = 5

if DEBUG:
    EMAIL_HOST = config('SMTP_SRV_DEBUG')
    EMAIL_PORT = 1025

RQ_QUEUES = {
    'default': {
        'URL': config('RQ_DJANGO_REDIS_URL'),
        'DEFAULT_TIMEOUT': 360,
    }
}
RQ_SHOW_ADMIN_LINK = True

RQ = {
    'DEFAULT_RESULT_TTL': 86400,
}

if not DEBUG:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    sentry_sdk.init(
        dsn=config('SENTRY_DSN'),
        integrations=[DjangoIntegration()],
        send_default_pii=True
    )

# CACHES = {
#     "default": {
#         'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#         "LOCATION": config('DJANGO_REDIS_URL'),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

logger.add(f"{LOGS_ROOT}/debug.log", filter=lambda record: record["level"].name == "DEBUG")
logger.add(f"{LOGS_ROOT}/info.log", filter=lambda record: record["level"].name == "INFO")
logger.add(f"{LOGS_ROOT}/error.log", filter=lambda record: record["level"].name == "ERROR")
