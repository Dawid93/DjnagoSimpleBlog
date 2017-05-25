# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20170525_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='series',
        ),
        migrations.AddField(
            model_name='post',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='posts.Series'),
        ),
    ]
