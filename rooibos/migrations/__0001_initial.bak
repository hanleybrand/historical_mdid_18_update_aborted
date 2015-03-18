# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core import validators
from django.db import models, migrations
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        # copied and pasted 0001_initial from site-packages/django/contrib/contenttypes/migrations/
        # ('contenttypes', '0001_initial'),
        # copied and pasted 0001_initial from site-packages/django/contrib/auth/migrations/0001_initial
        # ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # from contenttypes/migrations/0001_initial
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100, verbose_name='python model class name')),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'django_content_type',
                'verbose_name': 'content type',
                'verbose_name_plural': 'content types',
            },
            bases=(models.Model,),
        ),
        # from auth/migrations/0001_initial
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', to_field='id')),
                ('codename', models.CharField(max_length=100, verbose_name='codename')),
            ],
            options={
                'ordering': ('content_type__app_label', 'content_type__model', 'codename'),
                'unique_together': set([('content_type', 'codename')]),
                'verbose_name': 'permission',
                'verbose_name_plural': 'permissions',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80, verbose_name='name')),
                ('permissions', models.ManyToManyField(to='auth.Permission', verbose_name='permissions', blank=True)),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='AccessControl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(db_index=True)),
                ('read', models.NullBooleanField()),
                ('write', models.NullBooleanField()),
                ('manage', models.NullBooleanField()),
                ('restrictions_repr', models.TextField(default=b'', blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccumulatedActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(null=True, db_index=True)),
                ('date', models.DateField(db_index=True)),
                ('event', models.CharField(max_length=64, db_index=True)),
                ('final', models.BooleanField(default=False)),
                ('count', models.IntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
            options={

            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(null=True, db_index=True)),
                ('date', models.DateField(db_index=True)),
                ('time', models.TimeField()),
                ('event', models.CharField(max_length=64, db_index=True)),
                ('data_field', models.TextField(db_column=b'data', blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
                ('user_field', models.ForeignKey(db_column=b'user_id', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'access_attribute'
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
                ('attribute', models.ForeignKey(to='access_attribute.attribute')),
            ],
            options={
                'db_table': 'access_attributevalue'
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.SlugField(unique=True, blank=True)),
                ('hidden', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('agreement', models.TextField(null=True, blank=True)),
                ('password', models.CharField(max_length=32, blank=True)),
                ('children', models.ManyToManyField(to='rooibos.Collection', blank=True)),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CollectionItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hidden', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(to='rooibos.Collection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtendedGroup',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
                ('type', models.CharField(max_length=1, choices=[(b'A', b'Authenticated'), (b'I', b'IP Address based'), (b'P', b'Attribute based'), (b'E', b'Everybody')])),
            ],
            options={
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=100)),
                ('name', models.SlugField()),
                ('old_name', models.CharField(max_length=100, null=True, blank=True)),
                ('equivalent', models.ManyToManyField(related_name='equivalent_rel_+', null=True, to='rooibos.Field', blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.SlugField()),
                ('standard', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldSetField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=100, null=True, blank=True)),
                ('order', models.IntegerField(default=0)),
                ('importance', models.SmallIntegerField(default=1)),
                ('field', models.ForeignKey(to='rooibos.Field')),
                ('fieldset', models.ForeignKey(to='rooibos.FieldSet')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('refinement', models.CharField(max_length=100, null=True, blank=True)),
                ('label', models.CharField(max_length=100, null=True, blank=True)),
                ('hidden', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('group', models.IntegerField(null=True, blank=True)),
                ('value', models.TextField()),
                ('index_value', models.CharField(max_length=32, db_index=True)),
                ('date_start', models.DecimalField(null=True, max_digits=12, decimal_places=0, blank=True)),
                ('date_end', models.DecimalField(null=True, max_digits=12, decimal_places=0, blank=True)),
                ('numeric_value', models.DecimalField(null=True, max_digits=18, decimal_places=4, blank=True)),
                ('language', models.CharField(max_length=5, null=True, blank=True)),
                ('context_id', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisplayFieldValue',
            fields=[
                ('fieldvalue_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rooibos.FieldValue')),
            ],
            options={
            },
            bases=('rooibos.fieldvalue',),
        ),
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('func', models.CharField(max_length=128)),
                ('arg', models.TextField()),
                ('status', models.TextField(null=True, blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status_time', models.DateTimeField(null=True, blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('result', models.TextField()),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['completed', '-created_time'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField()),
                ('url', models.CharField(max_length=1024)),
                ('mimetype', models.CharField(default=b'application/binary', max_length=128)),
                ('width', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('bitrate', models.IntegerField(null=True)),
                ('master', models.ForeignKey(related_name='derivatives', to='rooibos.Media', null=True)),
            ],
            options={
                'verbose_name_plural': 'media',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MetadataStandard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.SlugField(unique=True)),
                ('prefix', models.CharField(unique=True, max_length=16)),
            ],
            options={
                'db_table': 'metadatastandard',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProxyUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(unique=True, max_length=36)),
                ('url', models.CharField(max_length=1024)),
                ('context', models.CharField(max_length=256, null=True, blank=True)),
                ('user_backend', models.CharField(max_length=256, null=True, blank=True)),
                ('last_access', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.SlugField(unique=True)),
                ('source', models.CharField(max_length=1024, null=True, blank=True)),
                ('manager', models.CharField(max_length=50, null=True, blank=True)),
                ('next_update', models.DateTimeField(null=True, blank=True)),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(blank=True, to='rooibos.Record', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.SlugField()),
                ('system', models.CharField(max_length=50)),
                ('base', models.CharField(help_text=b'Absolute path to server directory containing files.', max_length=1024, null=True)),
                ('urlbase', models.CharField(help_text=b'URL at which stored file is available, e.g. through streaming. May contain %(filename)s placeholder, which will be replaced with the media url property.', max_length=1024, null=True, verbose_name=b'URL base', blank=True)),
                ('deliverybase', models.CharField(db_column=b'serverbase', max_length=1024, blank=True, help_text=b'Absolute path to server directory in which a temporary symlink to the actual file should be created when the file is requested e.g. for streaming.', null=True, verbose_name=b'server base')),
                ('derivative', models.IntegerField(null=True, db_column=b'derivative_id')),
            ],
            options={
                'verbose_name_plural': 'storage',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subnet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subnet', models.CharField(max_length=80)),
                ('group', models.ForeignKey(to='rooibos.ExtendedGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='name', db_index=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(verbose_name='object id', db_index=True)),
                ('content_type', models.ForeignKey(verbose_name='content type', to='contenttypes.ContentType')),
                ('tag', models.ForeignKey(related_name='items', verbose_name='tag', to='rooibos.Tag')),
            ],
            options={
                'verbose_name': 'tagged item',
                'verbose_name_plural': 'tagged items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrustedSubnet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subnet', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.SlugField()),
                ('description', models.TextField(null=True, blank=True)),
                ('standard', models.NullBooleanField()),
                ('origin', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'vocabularies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VocabularyTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.TextField()),
                ('vocabulary', models.ForeignKey(to='rooibos.Vocabulary')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        # contenttypes/migrations/0001_initial
        migrations.AlterUniqueTogether(
            name='contenttype',
            unique_together=set([('app_label', 'model')]),
        ),
        migrations.AlterUniqueTogether(
            name='taggeditem',
            unique_together=set([('tag', 'content_type', 'object_id')]),
        ),
        migrations.AddField(
            model_name='proxyurl',
            name='subnet',
            field=models.ForeignKey(to='rooibos.TrustedSubnet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proxyurl',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='media',
            name='record',
            field=models.ForeignKey(to='rooibos.Record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='media',
            name='storage',
            field=models.ForeignKey(to='rooibos.Storage'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='media',
            unique_together=set([('record', 'name')]),
        ),
        migrations.AddField(
            model_name='fieldvalue',
            name='context_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fieldvalue',
            name='field',
            field=models.ForeignKey(to='rooibos.Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fieldvalue',
            name='owner',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fieldvalue',
            name='record',
            field=models.ForeignKey(editable=False, to='rooibos.Record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fieldset',
            name='fields',
            field=models.ManyToManyField(to='rooibos.Field', through='rooibos.FieldSetField'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fieldset',
            name='owner',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='field',
            name='standard',
            field=models.ForeignKey(blank=True, to='rooibos.MetadataStandard', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='field',
            name='vocabulary',
            field=models.ForeignKey(blank=True, to='rooibos.Vocabulary', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='field',
            unique_together=set([('name', 'standard')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='field',
            order_with_respect_to='standard',
        ),
        migrations.AddField(
            model_name='collectionitem',
            name='record',
            field=models.ForeignKey(to='rooibos.Record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='collection',
            name='records',
            field=models.ManyToManyField(to='rooibos.Record', through='rooibos.CollectionItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attribute',
            name='group',
            field=models.ForeignKey(to='rooibos.ExtendedGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accesscontrol',
            name='usergroup',
            field=models.ForeignKey(blank=True, to='auth.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='accesscontrol',
            unique_together=set([('content_type', 'object_id', 'user', 'usergroup')]),
        ),
    ]
