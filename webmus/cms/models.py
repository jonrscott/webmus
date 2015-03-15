from django.db import models

from .helpers import (
    simplify_html,
    process_content_for_display,
)


class BaseArticle(models.Model):
    slug = models.SlugField(db_index=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    thumbnail_image = models.BooleanField(default=False)
    content = models.TextField(blank=True)
    processed_content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['slug']

    @property
    def view_content(self):
        if self.processed_content is None and self.content is not None:
            self.save()
        return self.processed_content

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.title()

        if self.slug is None or self.slug.strip() == '':
            self.slug = self.title.lower().replace(' ', '')

        self.content = simplify_html(self.content)
        self.processed_content = process_content_for_display(self.content)
        super(BaseArticle, self).save(*args, **kwargs)


class Page(BaseArticle):
    max_articles = models.IntegerField(null=True, blank=True)


class Article(BaseArticle):
    class Meta:
        ordering = ['page', 'slug']

    page = models.ForeignKey(Page, related_name='articles')
    visible = models.BooleanField(default=True)
