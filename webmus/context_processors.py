from django.conf import settings


def config(request):
    webmus_config = settings.WEBMUS_CONFIG
    result = dict(webmus_config)
    menu_items = []
    for slug, page in webmus_config['pages'].items():
        if page.get('menu_order'):
            menu_items.append(dict(page, slug=slug))
    menu_items.sort(key=lambda x: x['menu_order'])
    result['menu_items'] = menu_items
    return {'webmus': result}
