from .models import MediaItem


def get_media(request):
    return [item.handler
            for item in MediaItem.objects.all().order_by('order')]
