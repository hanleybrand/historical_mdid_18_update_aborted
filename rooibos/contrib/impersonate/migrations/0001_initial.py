# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Impersonation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.ForeignKey(related_name='impersonating_set', to='auth.Group')),
                ('groups', models.ManyToManyField(related_name='impersonated_set', verbose_name=b'Allowed groups', to='auth.Group', blank=True)),
                ('users', models.ManyToManyField(related_name='impersonated_set', verbose_name=b'Allowed users', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
