# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-26 08:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0012_auto_20170226_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 26, 14, 29, 16, 700850)),
        ),
    ]