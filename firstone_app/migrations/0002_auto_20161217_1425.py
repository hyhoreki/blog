# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstone_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
