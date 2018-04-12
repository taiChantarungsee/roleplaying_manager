# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180412_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterbase',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
    ]
