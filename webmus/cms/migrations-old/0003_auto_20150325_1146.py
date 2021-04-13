# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20150315_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='narrow',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='narrow',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
