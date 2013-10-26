from django.contrib import admin

from .models import LinkCategory, Link

class LinkCategoryAdmin(admin.ModelAdmin):
    pass

class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(LinkCategory, LinkCategoryAdmin)
admin.site.register(Link, LinkAdmin)
