# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-11-19 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0074_auto_20201110_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengequestionnaire',
            name='challenge_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='challengequestionnaire',
            name='is_answered',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='challengequestionnaire',
            name='team_id',
            field=models.CharField(max_length=200),
        ),
    ]
