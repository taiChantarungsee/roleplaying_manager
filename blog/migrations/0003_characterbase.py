# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170715_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('race', models.CharField(default=b'human', max_length=5, choices=[(b'HUMAN', b'human'), (b'ELF', b'elf'), (b'DWARF', b'dwarf'), (b'ORC', b'orc')])),
                ('hometown', models.CharField(max_length=50)),
                ('likes', models.CharField(max_length=50)),
                ('relationships', models.CharField(max_length=50)),
            ],
        ),
    ]
