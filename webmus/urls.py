from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^files/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^$',
        'webmus.base.views.page_view',
        { 'page': 'home' },
        name='home'),
    #url(r'^projects/(?P<project>\w+)/$',
    #    'webmus.base.views.project_view',
    #    name='base_project'),
    url(r'^contact/$',
        'webmus.base.views.contact_view',
        name='base_contact'),
    url(r'^(?P<page>\w+)/$',
        'webmus.base.views.page_view',
        name='base_page'),
    url(r'^(?P<page>\w+)\.pdf$',
        'webmus.base.views.page_pdf_view',
        name='base_page_pdf'),
)
