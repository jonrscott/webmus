from django.db import models
from django.conf import settings

from ..musicdata.models import Artist, Venue


class Gig(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    artist = models.ForeignKey(Artist, blank=True, null=True)
    venue = models.ForeignKey(Venue)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='gigs', blank=True)

    @property
    def starts_at_short(self):
        if self.start_time:
            return "%s, %s" % (
                self.start_date.strftime(settings.SHORT_DATE_FORMAT),
                self.start_time.strftime(settings.TIME_FORMAT).lower())
        else:
            return self.start_date.strftime(settings.SHORT_DATE_FORMAT)

    @property
    def starts_at(self):
        if self.start_time:
            return "%s, %s" % (
                self.start_date.strftime(settings.DATE_FORMAT),
                self.start_time.strftime(settings.TIME_FORMAT).lower())
        else:
            return self.start_date.strftime(settings.DATE_FORMAT)

    @property
    def ends_at_short(self):
        if self.end_time:
            return "%s, %s" % (
                self.end_date.strftime(settings.SHORT_DATE_FORMAT),
                self.end_time.strftime(settings.TIME_FORMAT).lower())
        else:
            return self.end_date.strftime(settings.SHORT_DATE_FORMAT)

    @property
    def ends_at(self):
        if not self.end_date:
            return None
        if self.end_time:
            return "%s, %s" % (
                self.end_date.strftime(settings.DATE_FORMAT),
                self.end_time.strftime(settings.TIME_FORMAT))
        else:
            return self.end_date.strftime(settings.DATE_FORMAT)

    @property
    def short_date_string(self):
        if self.end_date:
            if self.end_date.month != self.start_date.month:
                return "%s - %s" % (self.starts_at_short, self.ends_at)
            return "%s - %s" % (self.starts_at_short, self.ends_at_short)
        return self.starts_at_short

    @property
    def full_date_string(self):
        if self.end_date:
            return "%s - %s" % (self.starts_at, self.ends_at)
        return self.starts_at

    @property
    def display_title(self):
        return self.title if self.title else self.artist

    def __unicode__(self):
        if self.title:
            return "%s: %s @ %s" % (self.starts_at, self.title, self.venue)
        else:
            return "%s: %s @ %s" % (self.starts_at, self.artist, self.venue)
