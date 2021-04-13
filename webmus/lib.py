import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context, TemplateDoesNotExist
from django.http import HttpResponse
from html import escape


def render_to_pdf(request, template_src, context_dict):
    if not isinstance(template_src, (str, unicode)):
        template = None
        while len(template_src):
            tmpl = template_src[0]
            template_src = template_src[1:]
            try:
                template = get_template(tmpl)
            except TemplateDoesNotExist:
                pass
        if template is None:
            raise TemplateDoesNotExist(tmpl)
    else:
        template = get_template(template_src)

    context_dict.update(pdf=True)
    context = Context(context_dict)
    html = template.render(context)
    result = io.StringIO()

    status = pisa.CreatePDF(io.StringIO(html.encode("UTF-8")), dest=result)
    if not status.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def sensible_title(str_):
    """
    Simpler title case than builtin, doesn't do weird things like "Thing'S".
    Prefix with a single '*' to treat everything afterwards as literal.
    Prefix with '**' to start with a single '*'.
    """
    if str_.startswith('*'):
        if str_.startwith('**'):
            str_ = str_[1:]
        else:
            return str_[1:]
    return ' '.join(s[0].upper() + s[1:].lower() for s in str_.split())
