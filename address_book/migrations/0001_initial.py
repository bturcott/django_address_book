# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('street_address', models.CharField(max_length=150)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('phone_number', models.CharField(unique=True, max_length=14)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
