from urlparse import (
    parse_qs,
    urlsplit,
)

from django.db import models

from ..musicdata.models import Artist, Venue

"""
# Media types:
#  youtube / vimeo / soundcloud
#

Common details:

Resource url
size?

"""


class MediaItem(models.Model):
    artist = models.ForeignKey(Artist, blank=True, null=True)
    venue = models.ForeignKey(Venue, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True, null=True)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        if self.artist:
            if self.title:
                return "%s - %s" % (self.artist, self.title)
            return unicode(self.artist)
        elif self.title:
            return self.title

    @property
    def handler(self):
        parts = urlsplit(self.url)
        query = parse_qs(parts.query)

        if 'youtube' in parts.netloc:
            return MediaHandlerYoutube(self, parts, query)
        elif 'vimeo' in parts.netloc:
            return MediaHandlerVimeo(self, parts, query)
        elif 'soundcloud' in parts.netloc:
            return MediaHandlerSoundcloud(self, parts, query)
        raise TypeError("Unsupported media type '%s'" % parts.netloc)


class MediaHandler(object):
    def __init__(self, item, parts, query):
        self._item = item
        self._parts = parts
        self._query = query

    def __unicode__(self):
        return unicode(self._item)

    @property
    def source(self):
        return type(self).__name__[12:].lower()

    @property
    def thumbnail_url(self):
        """Returning None means the embed must happen immediately"""
        return None

    @property
    def url(self):
        return self._item.url


class MediaHandlerYoutube(MediaHandler):
    @property
    def key(self):
        try:
            return self._query['v'][0]
        except:
            return None

    @property
    def embed_url(self):
        return '%s/embed/%s?showinfo=0&modestbranding=1' % (
            self.URL_BASE, self.youtube_key)

    @property
    def thumbnail_url(self):
        return "http://img.youtube.com/vi/%s/0.jpg" % self.key


class MediaHandlerVimeo(MediaHandler):
    @property
    def key(self):
        return self._parts.path.lstrip('/')


class MediaHandlerSoundcloud(MediaHandler):
    pass
