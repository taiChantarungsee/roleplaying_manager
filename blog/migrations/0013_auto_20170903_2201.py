# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_characterbase_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterbase',
            name='character_base_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
