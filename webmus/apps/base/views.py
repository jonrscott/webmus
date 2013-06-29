from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, TemplateDoesNotExist
from django import forms, http
from django.conf import settings

from ..contact.forms import ContactForm

from musweb.lib import render_to_pdf
from musweb.apps.links.models import LinkCategory
from musweb.apps.musicdata.models import Album
from musweb.apps.media.models import MediaVideo


def page_view(request, page, context={}):
    template = 'page/%s.html' % page
    context['page_slug'] = page
    try:
        return render_to_response(
            template, context,
            context_instance=RequestContext(request)
        )
    except TemplateDoesNotExist:
        raise http.Http404()


def page_pdf_view(request, page, context={}):
    template = 'page/%s.html' % page
    try:
        return render_to_pdf(
            template, {
                'pagesize':'A4',
            }
        )
    except TemplateDoesNotExist:
        raise http.Http404()



def contact_view(request):
    context = {}

    if request.method == 'POST':
        # handle contact
        form = ContactForm(request.POST, request=request)
        if form.is_valid():
            form.save()
    else:
        context['contact_form'] = ContactForm(request=request)

    return page_view(request, 'contact', context=context)


def links_view(request):
    return page_view(request, 'links', context={
        'categories': LinkCategory.objects.all().order_by('index')
    })


def discography_view(request):
    from musweb.apps.musicdata.helpers import get_albums_by_year
    return page_view(request, 'discography', context={
        'albums': get_albums_by_year(),
    })

def media_view(request):
    return page_view(request, 'media', context={
        'videos': MediaVideo.objects.all()
    })

def live_view(request):
    from musweb.apps.gigs.helpers import get_gigs_by_month
    return page_view(request, 'live', context={
        'gigs': get_gigs_by_month()
    })

def project_view(request, project=None, context={}):
    projects = settings.PROJECTS
    projects_dict = settings.PROJECTS_DICT

    if not project:
        return redirect('base_project', project=projects[0]['slug'])

    if project and project not in projects_dict:
        print "NO PROJECT!"
        raise http.Http404("Project '%s' not found" % project)
    template = 'projects/%s.html' % project
    context.update(
        page_slug = 'projects',
        project = projects_dict[project],
        projects = projects
    )
    try:
        return render_to_response(
            template, context,
            context_instance=RequestContext(request)
        )
    except TemplateDoesNotExist:
        print "NO TEMPLATE! %s" % template
        raise http.Http404()
