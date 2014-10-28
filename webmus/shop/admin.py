from django.contrib import admin

from .models import (
    ShopItem,
    ShopItemType,
    ShippingOption,
)


class ShopItemTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShopItemType, ShopItemTypeAdmin)


class ShippingOptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShippingOption, ShippingOptionAdmin)


class ShopItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShopItem, ShopItemAdmin)
