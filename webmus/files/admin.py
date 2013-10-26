from django.contrib import admin

from .models import UploadedFile, UploadedFileTag


class UploadedFileAdmin(admin.ModelAdmin):
    pass


class UploadedFileTagAdmin(admin.ModelAdmin):
    pass


admin.site.register(UploadedFile, UploadedFileAdmin)
admin.site.register(UploadedFileTag, UploadedFileTagAdmin)
