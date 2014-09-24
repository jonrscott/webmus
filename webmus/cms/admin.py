from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Page, Article


class BaseArticleAdmin(SummernoteModelAdmin):
    exclude = ('processed_content',)


class PageAdmin(BaseArticleAdmin):
    pass


class ArticleAdmin(BaseArticleAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(Article, ArticleAdmin)
