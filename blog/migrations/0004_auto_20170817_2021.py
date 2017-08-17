# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_characterbase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characterbase',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
