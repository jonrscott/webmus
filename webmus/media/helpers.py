from .models import MediaItem


def get_media():
    return [item.handler
            for item in MediaItem.objects.all().order_by('order')]
