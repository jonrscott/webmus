# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingoption',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
