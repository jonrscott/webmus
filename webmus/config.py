# Django settings required for webmus project.

#TEMPLATE_LOADERS = (
#    'django.template.loaders.app_directories.Loader',
#)

#MIDDLEWARE_CLASSES = (
#    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#)

#TEMPLATE_CONTEXT_PROCESSORS = [
#    'webmus.context_processors.thumbnails',
#]

#INSTALLED_APPS = (
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.messages',
#    'django.contrib.admin',
#
#    'sorl.thumbnail',
#
#    'webmus.apps.base',
#    'webmus.apps.contact',
#    'webmus.apps.links',
#    'webmus.apps.musicdata',
#    'webmus.apps.media',
#    'webmus.apps.gigs',
#)

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
