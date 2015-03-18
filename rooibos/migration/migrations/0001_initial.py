# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('m2m_object_id', models.PositiveIntegerField(null=True)),
                ('type', models.CharField(max_length=8, null=True, db_index=True)),
                ('original_id', models.CharField(max_length=255, db_index=True)),
                ('content_hash', models.CharField(max_length=32)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('m2m_content_type', models.ForeignKey(related_name='m2m_objecthistory_set', to='contenttypes.ContentType', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
