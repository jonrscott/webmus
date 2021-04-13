# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['page', 'slug']},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['slug']},
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail_image',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='visible',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='thumbnail_image',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
