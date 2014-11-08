from webmus.links.models import LinkCategory


def get_links():
    return LinkCategory.objects.all().order_by('index')
