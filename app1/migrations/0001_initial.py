# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_model',
            fields=[
                ('Activity_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Activity_Name', models.CharField(max_length=20)),
                ('Activity_type', models.CharField(max_length=20)),
                ('state', models.BooleanField(default=b'true')),
            ],
        ),
        migrations.CreateModel(
            name='detail_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Act_name', models.CharField(max_length=20)),
                ('emp_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='People_model',
            fields=[
                ('Id', models.IntegerField(primary_key=b'True', serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]