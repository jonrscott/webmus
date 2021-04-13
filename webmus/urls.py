from django.conf import settings
from django.urls import re_path, include
from django.views.static import serve as static_serve
from webmus.base.views import page_view, contact_view, page_pdf_view

urlpatterns = [
    re_path(r'^files/(?P<path>.*)$',
        static_serve,
        {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^summernote/', include('django_summernote.urls')),
    re_path(r'^$',
        page_view,
        { 'page': 'home' },
        name='home'),
    #re_path(r'^projects/(?P<project>\w+)/$',
    #    project_view,
    #    name='base_project'),
    re_path(r'^contact/$',
        contact_view,
        name='base_contact'),
    re_path(r'^(?P<page>\w+)/$',
        page_view,
        name='base_page'),
    re_path(r'^(?P<page>\w+)\.pdf$',
        page_pdf_view,
        name='base_page_pdf'),
]
