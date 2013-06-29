from django.contrib import admin

from .models import Gig


class GigAdmin(admin.ModelAdmin):
    pass


admin.site.register(Gig, GigAdmin)
