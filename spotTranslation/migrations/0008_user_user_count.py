# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-07-04 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotTranslation', '0007_auto_20190704_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_count',
            field=models.IntegerField(default=0),
        ),
    ]
