# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170206_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prop',
            name='sampled_feature',
        ),
        migrations.AddField(
            model_name='modelobject',
            name='sampled_feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sampling_feature', to='app.ModelObject'),
        ),
    ]
