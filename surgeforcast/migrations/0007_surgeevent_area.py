# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-25 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surgeforcast', '0006_auto_20180219_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='surgeevent',
            name='area',
            field=models.CharField(default='area', max_length=100),
            preserve_default=False,
        ),
    ]
