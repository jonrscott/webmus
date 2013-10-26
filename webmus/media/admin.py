from django.contrib import admin

from .models import MediaVideo

class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(MediaVideo, VideoAdmin)
