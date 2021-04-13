# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20150315_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='available',
            field=models.BooleanField(default=True, db_index=True),
        ),
    ]
