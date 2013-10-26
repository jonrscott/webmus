from django.db import models


from ..musicdata.models import Artist, Venue


class MediaItem(models.Model):
    artist = models.ForeignKey(Artist, blank=True, null=True)
    venue = models.ForeignKey(Venue, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        if self.artist:
            if self.title:
                return "%s - %s" % (self.artist, self.title)
            return unicode(self.artist)
        elif self.title:
            return self.title


class MediaVideo(MediaItem):
    URL_BASE = 'http://www.youtube.com'

    youtube_key = models.CharField(max_length=50)

    @property
    def url(self):
        return '%s/v/%s?fs=1&amp;hl=en_US&amp;rel=0' % (
            self.URL_BASE, self.youtube_key)

    @property
    def embed_url(self):
        return '%s/embed/%s?showinfo=0&modestbranding=1' % (
            self.URL_BASE, self.youtube_key)

    @property
    def thumbnail_url(self):
        return "http://img.youtube.com/vi/%s/3.jpg" % self.youtube_key
