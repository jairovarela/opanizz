# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0005_auto_20170920_0529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='fac_cliente',
            new_name='fac_client',
        ),
    ]