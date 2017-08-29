# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170821_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='allowed_supplements',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='dwarf',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='campaign',
            name='elf',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='campaign',
            name='human',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='campaign',
            name='min_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='orc',
            field=models.BooleanField(default=False),
        ),
    ]
