# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0013_auto_20170920_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duracionservicios',
            name='nombre',
            field=models.IntegerField(max_length=20, null=True, verbose_name='Cantidad de Tiempo'),
        ),
    ]
