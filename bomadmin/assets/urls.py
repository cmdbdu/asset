#!/usr/bin/env python
# coding:utf8
# By:dub
from django.conf.urls import patterns, include, url

urlpatterns = patterns('assets.views',
    url(r'^$', 'index', {'template':'assets/asset.html'}, name='asset'),
)
