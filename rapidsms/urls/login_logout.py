#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.urls import re_path
from .. import views

urlpatterns = (
    re_path(r'^login/$', views.RapidSMSLoginView.as_view(), name='rapidsms-login'),
    re_path(r'^logout/$', views.RapidSMSLogoutView.as_view(), name='rapidsms-logout'),
)
