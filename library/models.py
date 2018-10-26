# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

# 还书表
class Bookback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rid = models.ForeignKey('Readerinfo', models.DO_NOTHING, db_column='rid', blank=True, null=True)
    bid = models.ForeignKey('Bookinfo', models.DO_NOTHING, db_column='bid', blank=True, null=True)
    backtime = models.DateTimeField(blank=True, null=True)
    operator = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookback'


class Bookcase(models.Model):
    bcid = models.AutoField(primary_key=True)
    bcname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookcase'


class Bookcode(models.Model):
    bcode = models.IntegerField(primary_key=True)
    bid = models.ForeignKey('Bookinfo', models.DO_NOTHING, db_column='bid', blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookcode'


class Bookinfo(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=70, blank=True, null=True)
    btid = models.ForeignKey('Booktype', models.DO_NOTHING, db_column='btid', blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    bcid = models.ForeignKey(Bookcase, models.DO_NOTHING, db_column='bcid', blank=True, null=True)
    pubilshing = models.CharField(max_length=70, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookinfo'


class Booktype(models.Model):
    btid = models.AutoField(primary_key=True)
    typename = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booktype'


class Borrow(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rid = models.ForeignKey('Readerinfo', models.DO_NOTHING, db_column='rid', blank=True, null=True)
    bid = models.ForeignKey(Bookinfo, models.DO_NOTHING, db_column='bid', blank=True, null=True)
    borrowtime = models.DateTimeField(blank=True, null=True)
    backtime = models.DateTimeField(blank=True, null=True)
    operator = models.CharField(max_length=30, blank=True, null=True)
    ifback = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borrow'


class Library(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    libraryname = models.CharField(max_length=50, blank=True, null=True)
    curator = models.CharField(max_length=10, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(blank=True, null=True)
    introduce = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library'


class Manager(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.CharField(max_length=30, blank=True, null=True)
    pwd = models.CharField(max_length=30, blank=True, null=True)
    sysset = models.IntegerField(blank=True, null=True)
    readerset = models.IntegerField(blank=True, null=True)
    bookset = models.IntegerField(blank=True, null=True)
    borrowset = models.IntegerField(blank=True, null=True)
    sysquery = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class Readerinfo(models.Model):
    rid = models.AutoField(primary_key=True)
    rname = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)
    barcode = models.CharField(db_column='BARCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    vocation = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    papertype = models.CharField(db_column='paperType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paperno = models.CharField(db_column='PAPERNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=100, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='OPERATOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase.
    rtid = models.ForeignKey('Readertype', models.DO_NOTHING, db_column='rtid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'readerinfo'


class Readertype(models.Model):
    rtid = models.AutoField(primary_key=True)
    typename = models.CharField(max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    cprice = models.IntegerField(blank=True, null=True)
    validity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'readertype'
