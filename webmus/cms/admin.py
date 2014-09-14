from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Page, Article


class PageAdmin(SummernoteModelAdmin):
    pass


class ArticleAdmin(SummernoteModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(Article, ArticleAdmin)
