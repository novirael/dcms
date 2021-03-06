# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 09:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visits', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('number', models.CharField(max_length=32)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_prescription', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_prescription', to=settings.AUTH_USER_MODEL)),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='visits.Visit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('number', models.CharField(max_length=32)),
                ('is_invoice', models.BooleanField()),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_receipt', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_receipt', to=settings.AUTH_USER_MODEL)),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt', to='visits.Visit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('number', models.CharField(max_length=32)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_referral', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_referral', to=settings.AUTH_USER_MODEL)),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referral', to='visits.Visit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
