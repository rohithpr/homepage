# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150109_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='link',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
