from django.db import models

from .helpers import get_processed_content


class BaseArticle(models.Model):
    slug = models.SlugField(db_index=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    @property
    def processed_content(self):
        return self.get_processed_content()

    def get_processed_content(self):
        return get_processed_content(self.content)


class Page(BaseArticle):
    max_articles = models.IntegerField(null=True, blank=True)


class Article(BaseArticle):
    page = models.ForeignKey(Page, related_name='articles')
