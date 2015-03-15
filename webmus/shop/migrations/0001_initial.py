# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import webmus.shop.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model, webmus.shop.models.PriceMixin),
        ),
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
                ('price', models.IntegerField()),
                ('order', models.IntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model, webmus.shop.models.PriceMixin),
        ),
        migrations.CreateModel(
            name='ShopItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('default_price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shopitem',
            name='item_type',
            field=models.ForeignKey(to='shop.ShopItemType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shippingoption',
            name='item_type',
            field=models.ForeignKey(related_name=b'shipping_options', to='shop.ShopItemType'),
            preserve_default=True,
        ),
    ]
