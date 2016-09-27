#!/usr/bin/env python
# coding:utf8
# By:dub
from django import forms

from models import Assets
class AssetsFrom(forms.ModelForm):
    class Meta:
        model = Assets
        exclude = ['asset_status', 'asset_date', 'asset_to']
