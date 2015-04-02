import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context_dict.update(pdf=True)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
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
