# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20170903_2201'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dnd_character',
            new_name='DndCharacter',
        ),
        migrations.AddField(
            model_name='characterbase',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
