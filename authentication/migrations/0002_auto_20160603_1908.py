# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pesel',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name='customuser',
            name='post_code',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='customuser',
            name='telephone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='medical_right_number',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]