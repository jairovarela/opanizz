# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0006_auto_20170920_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fac_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.Contratado', verbose_name='Contrato'),
        ),
    ]
