# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-23 22:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20170923_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]