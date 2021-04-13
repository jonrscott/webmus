from django.core.management.base import BaseCommand
from django.conf import settings

from webmus.cms.models import Page


class Command(BaseCommand):
    help = "Create Page objects for all pages specified in settings"

    def handle(self, *args, **options):
        print "Creating missing pages"
        for slug, config in settings.WEBMUS_CONFIG['pages'].items():
            try:
                Page.objects.get(slug=slug)
                print " - %s already exists" % slug
            except Page.DoesNotExist:
                Page.objects.create(slug=slug, title=config['title'])
                print " - %s created" % slug
