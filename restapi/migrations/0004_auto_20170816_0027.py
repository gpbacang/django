# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_auto_20170816_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massprojectreport',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='massprojectreport',
            name='last_date',
            field=models.DateTimeField(),
        ),
    ]
