# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150109_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='glyphicon',
            field=models.CharField(default='', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='progress_bar_color',
            field=models.CharField(default='335544', max_length=6),
            preserve_default=True,
        ),
    ]
