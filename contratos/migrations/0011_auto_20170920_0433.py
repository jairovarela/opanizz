# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 08:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0010_contratado_modalidad_cuotas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contratado',
            options={'verbose_name': 'Cliente a Contratar', 'verbose_name_plural': 'Contratos Generados'},
        ),
    ]
