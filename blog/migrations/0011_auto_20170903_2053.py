# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170902_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='dnd_classes',
            fields=[
                ('classes_id', models.AutoField(serialize=False, primary_key=True)),
                ('fighter', models.BooleanField(default=False)),
                ('rouge', models.BooleanField(default=False)),
                ('cleric', models.BooleanField(default=False)),
                ('wizard', models.BooleanField(default=False)),
                ('barbarian', models.BooleanField(default=False)),
                ('bard', models.BooleanField(default=False)),
                ('druid', models.BooleanField(default=False)),
                ('monk', models.BooleanField(default=False)),
                ('sorceror', models.BooleanField(default=False)),
                ('warlock', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='id',
        ),
        migrations.AddField(
            model_name='characterbase',
            name='character_base_id',
            field=models.AutoField(default=uuid.uuid4, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='players',
            field=models.ManyToManyField(to='blog.Player', blank=True),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='campaigns',
            field=models.ManyToManyField(to='blog.Campaign', blank=True),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='dnd_character',
            fields=[
                ('characterbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='blog.CharacterBase')),
                ('dnd_classes_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='blog.dnd_classes')),
                ('hp', models.IntegerField(null=True, blank=True)),
                ('ac', models.IntegerField(null=True, blank=True)),
                ('movement_speed', models.IntegerField(null=True, blank=True)),
            ],
            bases=('blog.dnd_classes', 'blog.characterbase'),
        ),
    ]
