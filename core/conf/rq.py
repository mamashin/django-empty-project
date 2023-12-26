# -*- coding: utf-8 -*-
__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from decouple import config # noqa


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
