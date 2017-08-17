# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_remove_massprojectreport_last_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='massprojectreport',
            name='last_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]