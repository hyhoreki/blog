# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstone_app', '0002_auto_20161217_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('answer_user_id', models.IntegerField()),
                ('answer_question_id', models.IntegerField()),
                ('answer_text', models.TextField()),
                ('answer_time', models.DateTimeField(auto_now=True)),
                ('answer_agree', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Attention_question',
            fields=[
                ('aqid', models.AutoField(primary_key=True, serialize=False)),
                ('question_id', models.IntegerField()),
                ('attention_user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('friend_one', models.IntegerField(default=0)),
                ('friend_two', models.IntegerField(default=0)),
                ('friendship_status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('ask_user_id', models.IntegerField()),
                ('question_title', models.CharField(max_length=120)),
                ('question_describe', models.CharField(max_length=250)),
                ('question_text', models.TextField()),
                ('question_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Passage',
        ),
    ]
