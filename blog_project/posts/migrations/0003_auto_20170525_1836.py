# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170525_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location),
        ),
    ]
