# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170904_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='allowed_supplements',
        ),
        migrations.AlterField(
            model_name='campaign',
            name='system',
            field=models.CharField(max_length=15, blank=True, null=True, default='dnd', choices=[('DND', 'dnd'), ('FATE', 'fate'), ('SAVAGE_WORLDS', 'savage worlds'), ('BURNING_WHEEL', 'Burning Wheel')]),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='characterbase',
            name='race',
            field=models.CharField(max_length=5, blank=True, null=True, default='human', choices=[('HUMAN', 'human'), ('ELF', 'elf'), ('DWARF', 'dwarf'), ('ORC', 'orc')]),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='campaign',
            name='allowed_supplements',
            field=models.ManyToManyField(blank=True, to='blog.Supplement'),
        ),
    ]
