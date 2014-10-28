from .models import ShopItem


def get_shopfront():
    return ShopItem.objects.all().order_by('order')
