# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 22:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatmates', '0004_auto_20160726_0342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='Expenses',
        ),
    ]