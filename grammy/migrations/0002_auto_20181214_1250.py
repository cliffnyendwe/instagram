# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-14 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grammy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='Image_caption',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Bio',
            field=models.TextField(max_length=250),
        ),
    ]
