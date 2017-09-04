# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170904_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterbase',
            name='image',
            field=models.ImageField(default=1, upload_to=b'static/images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
