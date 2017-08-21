# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_characterbase_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('system', models.CharField(default=b'dnd', max_length=15, choices=[(b'DND', b'dnd'), (b'FATE', b'fate'), (b'SAVAGE_WORLDS', b'savage worlds'), (b'BURNING_WHEEL', b'Burning Wheel')])),
                ('gm_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('campaigns', models.ManyToManyField(to='blog.Campaign')),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='players',
            field=models.ManyToManyField(to='blog.Player'),
        ),
    ]
