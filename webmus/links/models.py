from django.db import models


class LinkCategory(models.Model):
    name = models.CharField('Name', max_length=100)
    index = models.IntegerField('Display Order', default=1)

    @property
    def links(self):
        return self.link_set.order_by('index')

    def __unicode__(self):
        return self.name


class Link(models.Model):
    category = models.ForeignKey(LinkCategory, null=True, on_delete=models.CASCADE)
    index = models.IntegerField('Display Order', default=1)
    name = models.CharField('Name', max_length=100)
    url = models.URLField('URL')
    description = models.CharField('Description', max_length=300, null=True, blank=True)

    def __unicode__(self):
        return self.name
