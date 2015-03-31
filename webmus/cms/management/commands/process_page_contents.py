from django.core.management.base import BaseCommand
from webmus.cms.models import Page, Article


class Command(BaseCommand):
    help = "Refresh processed content for all pages and articles"

    def handle(self, *args, **options):
        for page in Page.objects.all():
            print page.title
            page.processed_content = None
            page.save()

        for article in Article.objects.all():
            print article.title
            article.processed_content = None
            article.save()
