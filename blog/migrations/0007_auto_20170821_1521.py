# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170821_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='campaigns',
            field=models.ManyToManyField(to='blog.Campaign', blank=True),
        ),
    ]
