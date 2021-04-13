# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shippingoption_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingoption',
            name='order',
            field=models.IntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='order',
            field=models.IntegerField(default=0, db_index=True),
        ),
    ]
