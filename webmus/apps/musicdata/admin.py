from django.contrib import admin

from .models import Artist, Album, Venue


class ArtistAdmin(admin.ModelAdmin):
    pass


class VenueAdmin(admin.ModelAdmin):
    pass


class AlbumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Album, AlbumAdmin)
