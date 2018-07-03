# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    cache_key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client'


class CustomerInfo(models.Model):
    customer_id = models.AutoField(primary_key=True)
    condition = models.ForeignKey('CustomerCondition', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('CustomerSource', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('CustomerType', models.DO_NOTHING, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_sex = models.CharField(max_length=10, blank=True, null=True)
    customer_mobile = models.CharField(max_length=20, blank=True, null=True)
    customer_qq = models.CharField(max_length=20, blank=True, null=True)
    customer_address = models.CharField(max_length=500, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_remark = models.CharField(max_length=1000, blank=True, null=True)
    customer_job = models.CharField(max_length=100, blank=True, null=True)
    customer_blog = models.CharField(max_length=100, blank=True, null=True)
    customer_tel = models.CharField(max_length=20, blank=True, null=True)
    customer_msn = models.CharField(max_length=50, blank=True, null=True)
    birth_day = models.DateTimeField()
    customer_addtime = models.DateTimeField()
    customer_addman = models.CharField(max_length=50, blank=True, null=True)
    customer_changtime = models.DateTimeField()
    change_man = models.CharField(max_length=20, blank=True, null=True)
    customer_company = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_info'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
