# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20180412_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterbase',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
