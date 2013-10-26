from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^files/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'webmus.base.views.page_view',
        { 'page': 'home' }, name='home'),
    url(r'^live/$', 'webmus.base.views.live_view', name='base_live'),
    url(r'^media/$', 'webmus.base.views.media_view', name='base_media'),
    url(r'^discography/$', 'webmus.base.views.discography_view', name='base_discog'),
    url(r'^links/$', 'webmus.base.views.links_view', name='base_links'),
    url(r'^contact/$', 'webmus.base.views.contact_view', name='base_contact'),
    url(r'^projects/$', 'webmus.base.views.project_view', name='base_project'),
    url(r'^projects/(?P<project>\w+)/$', 'webmus.base.views.project_view', name='base_project'),
    url(r'^(?P<page>\w+)/$', 'webmus.base.views.page_view', name='base_page'),
    url(r'^(?P<page>\w+)\.pdf$', 'webmus.base.views.page_pdf_view', name='base_page_pdf'),

    # Examples:
    # url(r'^$', 'webmus.views.home', name='home'),
    # url(r'^webmus/', include('webmus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
