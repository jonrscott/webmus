from datetime import datetime

from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='artistimages', blank=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=200, blank=True)
    label = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(default=lambda: datetime.now().year)
    cover = models.ImageField(upload_to='albumcovers', blank=True)
    description = models.CharField(max_length=400, blank=True)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.artist, self.title)


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address_brief = models.CharField(max_length=100, blank=True)
    address_full = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        if self.address_brief:
            return "%s, %s" % (self.name, self.address_brief)
        return self.name
