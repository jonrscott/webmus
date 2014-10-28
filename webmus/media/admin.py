from django.contrib import admin

from .models import MediaItem


class MediaItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaItem, MediaItemAdmin)
