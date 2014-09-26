from importlib import import_module

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, TemplateDoesNotExist
from django import http
from django.conf import settings
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

from ..contact.forms import ContactForm

#from webmus.lib import render_to_pdf
from webmus.cms.models import Page
from webmus.links.models import LinkCategory
from webmus.media.models import MediaVideo


def page_view(request, page, context=None):
    context = context or {}
    templates = ['page/%s.html' % page,
                 'webmus/%s/default.html' % page]
    context['page_slug'] = page

    try:
        page_obj = Page.objects.get(slug=page)
        context['page_obj'] = page_obj
        templates.append('webmus/cms/managed_page.html')

        if page_obj.articles.count() > 0:
            paginator = Paginator(
                page_obj.articles.all().order_by('-created_at'),
                page_obj.max_articles or 5)
            page = request.GET.get('page')

            try:
                articles = paginator.page(page)
            except PageNotAnInteger:
                articles = paginator.page(1)
            except EmptyPage:
                articles = paginator.page(paginator.num_pages)
            context['articles'] = articles
    except Page.DoesNotExist:
        pass

    extra_context = getattr(settings, 'WEBMUS_CONFIG', {}).get(
        'pages', {}).get(page, {}).get('context', [])
    if isinstance(extra_context, dict):
        for key, val in extra_context.iteritems():
            if isinstance(val, basestring) and val.endswith(')'):
                base, args = val[:-1].rsplit('(', 1)
                args = [x.strip() for x in args.split(',') if len(x.strip())]
                module, fn = base.rsplit('.', 1)
                module = import_module(module)
                val = getattr(module, fn)
            if callable(val):
                val = val(*args)
            context[key] = val
    try:
        return render_to_response(
            templates, context,
            context_instance=RequestContext(request)
        )
    except TemplateDoesNotExist:
        raise http.Http404()


def page_pdf_view(request, page, context=None):
    pass
    #context = context or {}
    #template = 'page/%s.html' % page
    #try:
    #    return render_to_pdf(
    #        template, {
    #            'pagesize': 'A4',
    #        }
    #    )
    #except TemplateDoesNotExist:
    #    raise http.Http404()


def contact_view(request):
    context = {}

    if request.method == 'POST':
        # handle contact
        form = ContactForm(request.POST, request=request)
        if form.is_valid():
            form.save()
        else:
            context['contact_form' ] = form
    else:
        context['contact_form'] = ContactForm(request=request)

    return page_view(request, 'contact', context=context)


def links_view(request):
    return page_view(request, 'links', context={
        'categories': LinkCategory.objects.all().order_by('index')
    })


def discography_view(request):
    from webmus.musicdata.helpers import get_albums_by_year
    return page_view(request, 'discography', context={
        'albums': get_albums_by_year(),
    })


def media_view(request):
    return page_view(request, 'media', context={
        'videos': MediaVideo.objects.all()
    })


def live_view(request):
    from webmus.gigs.helpers import get_gigs_by_month
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
        page_slug='projects',
        project=projects_dict[project],
        projects=projects
    )
    try:
        return render_to_response(
            template, context,
            context_instance=RequestContext(request)
        )
    except TemplateDoesNotExist:
        print "NO TEMPLATE! %s" % template
        raise http.Http404()
