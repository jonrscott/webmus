from bs4 import BeautifulSoup
from bs4.element import NavigableString


def _wrap_things(soup, start, end, number):
    assert(start.parent == end.parent)
    wrapper = soup.new_tag(
        'div', **{'class': ['section'], 'id': 'section%d' % number})
    content = soup.new_tag(
        'div', **{'class': ['section-content']})
    wrapper.append(content)
    tag = start
    while tag is not None:
        next_tag = tag.next_sibling
        if tag == start:
            tag.replace_with(wrapper)
            content.append(tag)
        else:
            content.append(tag.extract())
        if tag == end:
            tag = None
        else:
            tag = next_tag
            if tag == end:
                content.append(tag.extract())
                tag = None


def prev_not_string(node):
    result = node.previous_sibling
    while isinstance(result, NavigableString):
        result = result.previous_sibling
    return result


def next_not_string(node):
    result = node.next_sibling
    while isinstance(result, NavigableString):
        result = result.next_sibling
    return result


def preprocess_html(fn):
    """
    Decorator to remove unwanted bits from html raw string.
    """
    def wrapped(html):
        return fn(html.replace('&nbsp;', ''))
    return wrapped


def html_fragment_processor(fn):
    """
    Decorator to use BeautifulSoup to process just a bit of html.
    """
    def wrapped(html):
        soup = BeautifulSoup(html)
        body = fn(soup, soup.body)
        return "\n".join(body.prettify().split('\n')[1:-1])
    return wrapped


@preprocess_html
@html_fragment_processor
def simplify_html(soup, body):
    """
    Cleanup dodgy Summernote HTML.
    Some day Summernote will do this already"""

    # no weird spans
    for span in body.find_all('span'):
        span.replace_with_children()

    # no <br>s
    for br in body.find_all('br'):
        br.extract()

    # no empty paras
    for p in body.find_all('p'):
        for thing in p.contents:
            if isinstance(thing, NavigableString) and thing.strip() == '':
                thing.extract()
        if len(p.contents) == 0:
            p.extract()

    # no inline styles!
    for el in body.find_all():
        if 'style' in el.attrs:
            del el.attrs['style']

    return body


@html_fragment_processor
def create_implied_sections(soup, body):
    """
    If a paragraph exists on its own containing just '---', then use that
    as a section marker, and jemmy the bits around it into
    <div class="section"> containers.

    So:
    <p>Blah</p>
    <p>---</p>
    <p>MoreBlah</p>

    becomes

    <div class="section section1">
    <p>Blah</p>
    </div>
    <div class="section section2">
    <p>MoreBlah</p>
    </div>
    """
    wrapped_start, wrapped_end = None, None
    next_section_number = 1
    wrapped_yet = False
    ps_to_extract = []
    for p in body.find_all('p', recursive=False):
        if (
                p.parent == body and
                len(p.contents) == 1 and
                isinstance(p.contents[0], NavigableString) and
                p.contents[0].strip() == '---'):

            if (    wrapped_start is None and
                    not wrapped_yet and
                    prev_not_string(p) is not None):
                wrapped_start = body.find_all()[0]

            if wrapped_start is None:
                wrapped_start = next_not_string(p)
            else:
                wrapped_end = prev_not_string(p)
                next_sibling = next_not_string(p)
                _wrap_things(
                    soup, wrapped_start, wrapped_end, next_section_number)
                next_section_number += 1
                wrapped_yet = True
                wrapped_start, wrapped_end = next_sibling, None
            ps_to_extract.append(p)

    for p in ps_to_extract:
        p.extract()

    if wrapped_start is not None and wrapped_end is None:
        wrapped_end = body.find_all(recursive=False)[-1]
        _wrap_things(
            soup, wrapped_start, wrapped_end, next_section_number)
        next_section_number += 1

    if next_section_number == 1:
        # have at least one section!
        all_things = body.find_all(recursive=False)
        if len(all_things) > 0:
            _wrap_things(soup, all_things[0], all_things[-1], 1)
        else:
            body.append(
                soup.new_tag('div', **{'class': 'section', 'id': 'section1'}))

    return body
