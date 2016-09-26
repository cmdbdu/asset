#coding:utf8

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    asset_edit = models.BooleanField(verbose_name=u'固资权限', default=False)
    parts_edit = models.BooleanField(verbose_name=u'生产权限', default=False)

    def __unicode__(self):
        return self.user.username
#
    class Meta:
        db_table = 'account_profile'
#
#
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'asset_edit', 'parts_edit']
