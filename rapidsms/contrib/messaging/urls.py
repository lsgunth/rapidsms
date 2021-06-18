#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.conf.urls import re_path
from . import views


urlpatterns = (
    re_path(r'^$', views.messaging, name='messaging'),
    re_path(r'^send/$', views.send, name='send_message'),
)
