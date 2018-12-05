# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-28 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.IntegerField(max_length=64)),
                ('c_positid', models.CharField(max_length=7, unique=True)),
                ('c_title', models.CharField(max_length=50)),
                ('c_image', models.CharField(max_length=200)),
                ('c_duration', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_positid', models.CharField(max_length=7, unique=True)),
                ('m_title', models.CharField(max_length=50)),
                ('m_image', models.CharField(max_length=200)),
                ('m_duration', models.CharField(max_length=100)),
                ('m_appfutitle', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=16, null=True, unique=True)),
                ('u_icon', models.ImageField(upload_to='%Y/%m/%d/icons')),
                ('u_password', models.CharField(max_length=16)),
                ('u_email', models.CharField(max_length=25)),
            ],
        ),
    ]
