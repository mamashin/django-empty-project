# -*- coding: utf-8 -*-
__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from decouple import config # noqa


DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
AUTH_USER_MODEL = 'users.User'
WSGI_APPLICATION = 'core.wsgi.application'
ROOT_URLCONF = 'core.urls'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

USE_I18N = True
USE_L10N = True
USE_TZ = True


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'core.middleware.CustomRemoteUserBackend',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

EMAIL_HOST = config('SMTP_SRV')
EMAIL_PORT = 25
EMAIL_TIMEOUT = 5

if DEBUG:
    EMAIL_HOST = config('SMTP_SRV_DEBUG')
    EMAIL_PORT = 1025

CSRF_TRUSTED_ORIGINS = ["https://bot.food-com.ru"]
