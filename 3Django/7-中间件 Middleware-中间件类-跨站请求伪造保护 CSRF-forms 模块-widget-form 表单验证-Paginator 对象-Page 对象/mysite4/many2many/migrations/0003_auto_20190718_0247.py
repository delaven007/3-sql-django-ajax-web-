# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-18 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('many2many', '0002_book3_authors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auther3',
            new_name='Author3',
        ),
    ]
