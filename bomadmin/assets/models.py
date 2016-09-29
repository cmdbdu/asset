#coding:utf8
import time

from django.db import models
from django.contrib import admin

class Assets(models.Model):
    ASSET_CHOISE_STATUS = (
            ('store', u'库存中'),
            ('inuse', u'使用中')
            )
    asset_sn = models.CharField(max_length=200, verbose_name=u'SN')
    asset_type = models.CharField(max_length=200, verbose_name=u'固资种类')
    asset_model = models.CharField(max_length=200, verbose_name=u'固资型号')
    asset_factory = models.CharField(max_length=200, verbose_name=u'厂家')
    asset_from = models.CharField(max_length=200, verbose_name=u'采购来源')
    asset_to = models.CharField(max_length=200, verbose_name=u'固资去向',
                                blank=True)
    asset_status = models.CharField(max_length=200, verbose_name=u'固资状态',
                                choices=ASSET_CHOISE_STATUS, default='store')
    asset_date = models.CharField(max_length=200, verbose_name=u'采购时间',
                                 default=time.strftime('%Y-%m-%d'))

