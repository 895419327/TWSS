# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170818_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='praticecourse',
            name='classes',
            field=models.CharField(default='未记录', max_length=128),
        ),
        migrations.AddField(
            model_name='praticecourse',
            name='student_sum',
            field=models.IntegerField(default=0, verbose_name=1024),
        ),
        migrations.AddField(
            model_name='theorycourse',
            name='classes',
            field=models.CharField(default='未记录', max_length=128),
        ),
        migrations.AddField(
            model_name='theorycourse',
            name='student_sum',
            field=models.IntegerField(default=0, verbose_name=1024),
        ),
    ]