# -*- coding: utf-8 -*-

__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules
# import django_rq
from datetime import datetime
from django.conf import settings


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        # Automatically import all receivers files
        autodiscover_modules('receivers')

        # if not settings.DEBUG:
        #     scheduler = django_rq.get_scheduler('default')
        #     # Delete any existing jobs in the scheduler when the app starts up
        #     for job in scheduler.get_jobs():
        #         job.delete()
        #
        #     scheduler.schedule(datetime.utcnow(), test_job, interval=60, repeat=5, result_ttl=3600)
