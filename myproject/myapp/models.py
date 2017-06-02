# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib  import admin

# Create your models here.
class Group(models.Model):
    name = models.CharField(u'业务组', max_length=30)
    leader = models.CharField(u'负责人', max_length=30)

class Business(models.Model):
    name = models.CharField(u'业务名称', max_length=30)
    creator = models.CharField(u'创建人', max_length=30)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    members = models.IntegerField(u'用户数', default=0)
    group = models.ForeignKey(Group, verbose_name = u'所属业务组')

class  AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader')

admin.site.register(Group, AppAdmin)

