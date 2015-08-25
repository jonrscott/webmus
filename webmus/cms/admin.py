from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Page, Article


class BaseArticleAdmin(SummernoteModelAdmin):
    exclude = ('slug', 'processed_content',)


class PageAdmin(BaseArticleAdmin):
    pass


class ArticleAdmin(BaseArticleAdmin):
    list_display = ['title', 'page']

    def get_fields(self, request, obj=None):
        result = super(ArticleAdmin, self).get_fields(request, obj=obj)
        result.remove('page')
        result.insert(0, 'page')
        return result


admin.site.register(Page, PageAdmin)
admin.site.register(Article, ArticleAdmin)
