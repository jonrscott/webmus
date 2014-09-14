from django.conf import settings


def config(request):
    webmus_config = settings.WEBMUS_CONFIG
    result = dict(webmus_config)
    menu_items = []
    for slug, page in webmus_config['pages'].iteritems():
        if page.get('menu_order'):
            menu_items.append(dict(page, slug=slug))
    menu_items.sort(key=lambda x: x['menu_order'])
    result['menu_items'] = menu_items
    print "setting webmus to", result
    return {'webmus': result}


def thumbnails(request):
    return dict(
        ('thumbnail_' + key, val) for (key, val) in
        settings.THUMBNAIL_SIZES.items())
