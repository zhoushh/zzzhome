# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Feedback(models.Model):
    idfeedback = models.AutoField(primary_key=True)
    text = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'feedback'


class Item(models.Model):
    iditem = models.AutoField(primary_key=True)
    itemname = models.CharField(db_column='itemName', max_length=45)  # Field name made lowercase.
    itemstatus = models.CharField(db_column='itemStatus', max_length=10)  # Field name made lowercase.
    itempstn = models.ForeignKey('Position', models.DO_NOTHING, db_column='itemPstn')  # Field name made lowercase.
    itemnote = models.CharField(db_column='itemNote', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itemmodtime = models.DateTimeField(db_column='itemModTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item'


class Position(models.Model):
    idposition = models.AutoField(primary_key=True)
    room = models.ForeignKey('Room', models.DO_NOTHING, db_column='room')
    container = models.CharField(max_length=45)
    block = models.CharField(max_length=45)
    pstnnote = models.CharField(db_column='pstnNote', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.room) + self.container + self.block

    class Meta:
        managed = False
        db_table = 'position'


class Room(models.Model):
    idroom = models.AutoField(primary_key=True)
    roomname = models.CharField(db_column='roomName', unique=True, max_length=10)  # Field name made lowercase.

    def __str__(self):
        return self.roomname

    class Meta:
        managed = False
        db_table = 'room'
