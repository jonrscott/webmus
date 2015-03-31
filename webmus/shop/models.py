from django.db import models
from django.conf import settings


class PriceMixin(object):
    @property
    def price_str_no_unit(self):
        return '%d.%2.2d' % (
            self.price / 100,
            self.price % 100
        )

    @property
    def price_str(self):
        return settings.WEBMUS_CONFIG['shop_currency_format'] % (
            self.price_str_no_unit)


class ShopItemType(models.Model):
    name = models.CharField(max_length=100)
    default_price = models.IntegerField()       # pence

    def __unicode__(self):
        return self.name


class ShippingOption(models.Model, PriceMixin):
    order = models.IntegerField(default=0, db_index=True)
    item_type = models.ForeignKey(
        ShopItemType, related_name='shipping_options')
    name = models.CharField(max_length=100)
    price = models.IntegerField()       # pence

    def __unicode__(self):
        return "%s - %s" % (self.item_type, self.name)


class ShopItem(models.Model, PriceMixin):
    item_type = models.ForeignKey(ShopItemType)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()       # pence
    order = models.IntegerField(default=0, db_index=True)
    available = models.BooleanField(default=True, db_index=True)

    def __unicode__(self):
        return self.title

    @property
    def shipping_options(self):
        return self.item_type.shipping_options.all().order_by('order')
