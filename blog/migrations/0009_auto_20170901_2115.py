# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170828_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterbase',
            name='campaigns',
            field=models.ManyToManyField(to='blog.Campaign', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='first_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='hometown',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='likes',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='race',
            field=models.CharField(default=b'human', max_length=5, null=True, blank=True, choices=[(b'HUMAN', b'human'), (b'ELF', b'elf'), (b'DWARF', b'dwarf'), (b'ORC', b'orc')]),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='relationships',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
