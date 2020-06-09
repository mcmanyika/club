# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-11 04:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import siteInfo.models


class Migration(migrations.Migration):

    dependencies = [
        ('siteInfo', '0003_remove_t_urls_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_sub_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
                ('link', models.CharField(default='', max_length=120)),
                ('category', models.CharField(default='', max_length=120)),
                ('icon', models.FileField(blank=True, null=True, upload_to=siteInfo.models.upload_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rootid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteInfo.t_urls')),
            ],
        ),
    ]