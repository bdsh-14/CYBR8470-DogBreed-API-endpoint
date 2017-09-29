# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_breed_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='exerciseneeds',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='sheddingamount',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='breed',
            name='size',
            field=models.CharField(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.IntegerField(),
        ),
    ]
