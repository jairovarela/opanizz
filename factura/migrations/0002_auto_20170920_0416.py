# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='num_fact',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Numero de Factura'),
        ),
    ]
