from django.conf import settings

def thumbnails(request):
    return dict(('thumbnail_'+key, val) for (key, val) in 
            settings.THUMBNAIL_SIZES.items())
