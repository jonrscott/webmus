from django.urls import reverse
from .models import ShopItem


def get_shopfront(request):
    return ShopItem.objects.filter(available=True).order_by('order')


def get_shop_uri(request):
    return request.build_absolute_uri(
        reverse('base_page', kwargs={'page': 'shop'}))
