from .models import ShopItem


def get_shopfront():
    return ShopItem.objects.filter(available=True).order_by('order')
