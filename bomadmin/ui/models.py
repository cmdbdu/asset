# coding:utf-8
from django.db import models

class Bom(models.Model):
    bom_name choice
    bom_sn
    bom_date
    bom_pri
    bom_type 

class Device(models.Model):
    device_type
    device_sn
    device_name
    device_date

