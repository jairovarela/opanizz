# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-21 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0016_auto_20170921_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='precio_beneficiario',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio por cada Beneficiario'),
        ),
    ]
