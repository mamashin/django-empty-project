# -*- coding: utf-8 -*-

__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    # path('api/', include('core.api.urls')),
    path('admin/', admin.site.urls),
    path('django-rq/', include('django_rq.urls')),
    path('sentry-debug/', trigger_error),
    path('', include('core.urls')),
]
