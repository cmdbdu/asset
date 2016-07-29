#!/usr/bin/env python
# coding:utf8
# By:dub
from django import forms

from models import Customer, Bom, Device

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer


class BomForm(forms.ModelForm):

    class Meta:
        model = Bom
        exclude = ['bom_date', 'bom_status']


class DeviceForm(forms.Form):
    device_sn = forms.CharField(max_length=50)

    #class Meta:
    #    model = Device
    #    exclude = ['device_date']


