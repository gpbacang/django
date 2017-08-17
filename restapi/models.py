# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class MassProject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=13)

class MassProjectReport(models.Model):
    id = models.IntegerField(primary_key=True)
    e_sent = models.IntegerField()
    initial = models.IntegerField()
    subscribed = models.IntegerField()
    unsubscribed = models.IntegerField()
    bounced = models.IntegerField()
    mozart_rows = models.IntegerField()
    e_sent_today = models.IntegerField()
    e_sent_week = models.IntegerField()
    e_sent_month = models.IntegerField()
    freq_0 = models.IntegerField()
    freq_1m = models.IntegerField()
    freq_3m = models.IntegerField()
    freq_6m = models.IntegerField()
    freq_recu_4m = models.IntegerField()
    # last_date = models.DateTimeField()
    project_id = models.IntegerField()
    created_at = models.DateTimeField()
