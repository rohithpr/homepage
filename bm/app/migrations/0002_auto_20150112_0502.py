# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('link', models.TextField()),
                ('glyphicon', models.CharField(max_length=30)),
                ('category', models.ForeignKey(to='app.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='glyphicon',
            field=models.CharField(default='asterisk', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='progress_bar_color',
            field=models.CharField(default='335544', max_length=6),
            preserve_default=True,
        ),
    ]
