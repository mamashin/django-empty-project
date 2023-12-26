# -*- coding: utf-8 -*-
__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import MainPage

api = [
    path("v1/", include("core.urls.v1")),
]

urlpatterns = [
    path("api/", include(api)),
    path("admin/", admin.site.urls),
    path('django-rq/', include('django_rq.urls')),
    path('', MainPage.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
