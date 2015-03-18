# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rooibos', '0002_auto_20150317_2124'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.SlugField(unique=True)),
                ('hidden', models.BooleanField(default=False)),
                ('source', models.CharField(max_length=1024, null=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('password', models.CharField(max_length=32, null=True, blank=True)),
                ('hide_default_data', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('fieldset', models.ForeignKey(to='rooibos.FieldSet', null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('publish_presentations', 'Can publish presentations'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PresentationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hidden', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=16, blank=True)),
                ('order', models.SmallIntegerField()),
                ('presentation', models.ForeignKey(related_name='items', to='presentation.Presentation')),
                ('record', models.ForeignKey(to='rooibos.Record')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PresentationItemInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.TextField(blank=True)),
                ('item', models.ForeignKey(related_name='media', to='presentation.PresentationItem')),
                ('media', models.ForeignKey(to='rooibos.Media')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
