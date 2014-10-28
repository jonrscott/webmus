# Django settings required for webmus project.

TEMPLATE_CONTEXT_PROCESSORS = (
    'webmus.context_processors.config',
    'webmus.context_processors.thumbnails',
)

INSTALLED_APPS = (
    'easy_thumbnails',

    'webmus.cms',
    'webmus.base',
    'webmus.contact',
    'webmus.links',
    'webmus.musicdata',
    'webmus.media',
    'webmus.gigs',
    'webmus.shop',
)

THUMBNAIL_SIZES = {
    'album': '60',
}

SHORT_DATE_FORMAT = "%a %d"
DATE_FORMAT = "%d %b %y"
TIME_FORMAT = "%I:%M%p"

#PROJECTS = (
#    {
#        'name': "My Project",
#        'slug': 'myproject',
#    },
#)
PROJECTS = ()

PROJECTS_DICT = dict((p['slug'], p) for p in PROJECTS)

SUMMERNOTE_CONFIG = {
    'toolbar': [
        ['style', ['style']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol']],
        ['insert', ['link', 'table']],
        ['insert', ['picture', 'video']],
        ['misc', ['undo', 'redo']],
        ['misc', ['codeview']],
    ],
    'styleWithSpan': False,
    'disableDragAndDrop': True,
}
