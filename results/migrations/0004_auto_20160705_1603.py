# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-05 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20160704_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctions',
            name='bids',
            field=models.CharField(default='', max_length=300, null=True),
        ),
    ]