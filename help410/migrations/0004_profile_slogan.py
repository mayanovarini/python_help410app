# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-05 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help410', '0003_auto_20160705_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slogan',
            field=models.CharField(default='My slogan', max_length=500),
            preserve_default=False,
        ),
    ]
