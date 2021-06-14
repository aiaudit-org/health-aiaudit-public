# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-11-10 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0012_remove_docker_repository_uri_from_team'),
        ('challenges', '0073_add_inform_hosts_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_answered', models.BooleanField(default=False)),
                ('answ_one', models.CharField(max_length=200)),
                ('answ_two', models.CharField(max_length=200)),
                ('answ_three', models.CharField(max_length=200)),
                ('answ_four', models.CharField(max_length=200)),
                ('answ_five', models.CharField(max_length=200)),
                ('answ_six', models.CharField(max_length=200)),
                ('answ_seven', models.CharField(max_length=200)),
                ('answ_eight', models.CharField(max_length=200)),
                ('answ_nine', models.CharField(max_length=200)),
                ('answ_ten', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'questionnaire_data',
            },
        ),
        migrations.AlterField(
            model_name='challenge',
            name='worker_cpu_cores',
            field=models.IntegerField(blank=True, default=256, null=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='worker_memory',
            field=models.IntegerField(blank=True, default=512, null=True),
        ),
        migrations.AddField(
            model_name='challengequestionnaire',
            name='challenge_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.Challenge'),
        ),
        migrations.AddField(
            model_name='challengequestionnaire',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.ParticipantTeam'),
        ),
    ]