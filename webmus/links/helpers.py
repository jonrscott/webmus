from webmus.links.models import LinkCategory


def get_links(request):
    return LinkCategory.objects.all().order_by('index')
