# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_bookmark_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='link',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
