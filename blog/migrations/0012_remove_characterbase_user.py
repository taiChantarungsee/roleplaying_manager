# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170903_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterbase',
            name='user',
        ),
    ]
