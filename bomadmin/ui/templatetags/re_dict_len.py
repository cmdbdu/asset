#!/usr/bin/env python
# coding:utf8
# By:dub
from django import template

register = template.Library()


def dictl(dicts):
    keys = dicts.keys()
    return len(keys)


register.filter('dictl',dictl)
