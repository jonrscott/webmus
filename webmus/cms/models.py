from django.db import models

from .helpers import (
    simplify_html,
    create_implied_sections,
)


class BaseArticle(models.Model):
    slug = models.SlugField(db_index=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(blank=True)
    processed_content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def view_content(self):
        if self.processed_content is None and self.content is not None:
            self.save()
        return self.processed_content

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content = simplify_html(self.content)
        self.processed_content = create_implied_sections(self.content)
        super(BaseArticle, self).save(*args, **kwargs)


class Page(BaseArticle):
    max_articles = models.IntegerField(null=True, blank=True)


class Article(BaseArticle):
    page = models.ForeignKey(Page, related_name='articles')
