# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0007_auto_20171227_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdistribution',
            name='dist_date',
            field=models.DateField(verbose_name='分配日期'),
        ),
        migrations.AlterField(
            model_name='customerdistribution',
            name='memo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='更多信息'),
        ),
    ]