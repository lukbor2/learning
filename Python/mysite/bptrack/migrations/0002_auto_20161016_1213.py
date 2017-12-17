# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-16 19:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bptrack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bp_measure',
            name='bp_measure_date',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 10, 16, 19, 13, 34, 609797, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bp_measure',
            name='bp_measure_max',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bp_measure',
            name='bp_measure_min',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bp_measure',
            name='bp_measure_pulse',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]