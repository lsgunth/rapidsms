#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.urls import re_path
from . import views


urlpatterns = (
    re_path(r'^$', views.registration, name="registration"),
    re_path(r'^contact/add/$', views.contact, name="registration_contact_add"),
    re_path(r'^contact/bulk_add/$', views.contact_bulk_add, name="registration_bulk_add"),
    re_path(r'^(?P<pk>\d+)/edit/$', views.contact, name="registration_contact_edit"),
)
