# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from logmail.urls import urlpatterns as logmail_urls

urlpatterns = [
    url(r'^', include(logmail_urls, namespace='logmail')),
]
