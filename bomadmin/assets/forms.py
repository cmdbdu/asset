#!/usr/bin/env python
# coding:utf8
# By:dub
from django import forms

from models import Assets
class AssetsFrom(forms.ModelForm):
    class Meta:
        model = Assets
