# coding:utf8
import time

from django.db import models
from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

class Customer(models.Model):
    cus_name = models.CharField(max_length=200, verbose_name=u'客户名称')
    cus_tele = models.CharField(max_length=200, verbose_name=u'联系电话')
    cus_addr = models.CharField(max_length=200, verbose_name=u'联系地址')
    cus_user = models.CharField(max_length=200, verbose_name=u'联系人')

    def __unicode__(self): # PY3 change to __str__
        return self.cus_name

    class Meta:
        verbose_name = u'用户信息'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cus_name',
                    'cus_user',
                    'cus_tele',
                    'cus_addr')


class Bom(models.Model):
    BOM_CHOICES_NAME = (
            ('hba',u"HBA卡"),
            ('mem',u"内存条"),
            ('ser',u"服务器"),
            ('disk',u"硬盘"),
            )
    BOM_CHOICES_STATE = (
            ('store', u'库存'),
            ('inuse', u'使用中'),
            )
    bom_status = models.CharField(max_length=20,verbose_name=u'状态',
                                choices=BOM_CHOICES_STATE,
                                default='store')
    bom_name = models.CharField(max_length=200, choices=BOM_CHOICES_NAME,
                                verbose_name=u'名称')
    bom_sn = models.CharField(max_length=200, verbose_name=u'编码', unique=True)
    bom_date = models.CharField(max_length=200, verbose_name=u'时间',
                                default=time.strftime('%Y-%m-%d'))
    #bom_pri = models.CharField(max_length=200, verbose_name=u'价格')
    bom_type = models.CharField(max_length=200, verbose_name=u'型号')

    def __unicode__(self):
        return self.bom_sn

    class Meta:
        verbose_name = u'物料'


class BomAdmin(admin.ModelAdmin):
    list_display = ('bom_name',
                    'bom_sn',
                    'bom_date',
                    'bom_date',
#                    'bom_pri',
                    'bom_type')


class Device(models.Model):
# TODO auto create
    #device_type = models.CharField(max_length=200, verbose_name=u'型号')
    #device_name = models.CharField(max_length=200, verbose_name=u'名称')
    DEVICE_CHOICES_STATE = (
            ('store', u'库存'),
            ('inuse', u'使用中'),
            )
    device_status = models.CharField(max_length=200,verbose_name=u'状态',
                                choices=DEVICE_CHOICES_STATE,
                                default='store')
    device_sn = models.CharField(max_length=200, verbose_name=u'编码',
                                blank=True)
    device_date = models.CharField(max_length=200, verbose_name=u'日期',
                                default=time.strftime('%Y-%m-%d'))
    device_user = models.OneToOneField(Customer, verbose_name=u'用户',
                                null=True)
    device_boms = models.ManyToManyField(Bom, verbose_name=u'配件')



    class Meta:
        verbose_name = u"产品"


class DeviceAdmin(admin.ModelAdmin):

    list_display = ('device_user',
                    'device_date',
                    'device_sn'
                    )
    def device_sn(self, obj):
        for a in obj.device_boms.all():
            print a.bom_name
            if a.bom_name == 'ser':
                return a.bom_sn

