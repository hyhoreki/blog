# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstone_app', '0003_auto_20170118_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_describe',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.CharField(max_length=30),
        ),
    ]
