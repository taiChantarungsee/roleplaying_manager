# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170901_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='allowed_supplements',
            field=models.TextField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='gm_name',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='min_level',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='players',
            field=models.ManyToManyField(to='blog.Player', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='system',
            field=models.CharField(default=b'dnd', max_length=15, null=True, blank=True, choices=[(b'DND', b'dnd'), (b'FATE', b'fate'), (b'SAVAGE_WORLDS', b'savage worlds'), (b'BURNING_WHEEL', b'Burning Wheel')]),
        ),
    ]
