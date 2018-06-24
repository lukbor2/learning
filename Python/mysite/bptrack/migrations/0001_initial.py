# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-01 03:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BP_Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bp_measure_date', models.DateField(default=datetime.date.today, help_text='Day when the measure was taken')),
                ('bp_measure_min', models.IntegerField(help_text='Min pressure in mmHG')),
                ('bp_measure_max', models.IntegerField(help_text='Max pressure in mmHG')),
                ('bp_measure_pulse', models.IntegerField(help_text='Pulse when the measure was taken')),
                ('bp_measure_time_of_day', models.CharField(choices=[('MO', 'Morning'), ('AF', 'Afternoon'), ('EV', 'Evening')], help_text='Pick one of the categories depending on the time when the measure was taken', max_length=30)),
                ('bp_measure_note', models.CharField(blank=True, help_text='Free text', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AddField(
            model_name='bp_measure',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bptrack.Patient'),
        ),
    ]
