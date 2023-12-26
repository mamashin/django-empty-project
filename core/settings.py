# -*- coding: utf-8 -*-
__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from pathlib import Path
from decouple import config # noqa
from split_settings.tools import include


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
ROOT_DIR = BASE_DIR.parent
APPS_DIR = BASE_DIR / 'apps'
LOGS_ROOT = BASE_DIR / 'logs'

include(
    'conf/common.py',
    'conf/installed_apps.py',
    'conf/db.py',
    'conf/rest.py',
    'conf/media.py',
    'conf/templates.py',
    'conf/middleware.py',
    'conf/rq.py',
    'conf/logging.py',
    'conf/cache.py',
)
