# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 01:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_site',
            new_name='profile_pics',
        ),
    ]
