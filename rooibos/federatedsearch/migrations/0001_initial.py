# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(max_length=255, db_index=True)),
                ('source', models.CharField(max_length=32, db_index=True)),
                ('hits', models.IntegerField()),
                ('results', models.TextField(null=True, blank=True)),
                ('valid_until', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SharedCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.SlugField(unique=True, blank=True)),
                ('e_url', models.TextField(blank=True)),
                ('e_username', models.TextField(blank=True)),
                ('e_password', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
    ]
