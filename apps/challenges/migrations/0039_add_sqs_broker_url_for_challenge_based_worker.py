# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-12 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0038_challenge_remote_evaluation")]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="broker_url",
            field=models.CharField(
                db_index=True,
                default="",
                max_length=200,
                verbose_name="SQS queue name",
            ),
        )
    ]