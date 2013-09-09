from django import template
from django.template import defaultfilters


register = template.Library()


@register.filter(is_safe=True)
@defaultfilters.stringfilter
def renderimages(value, model):
    """
    Convert or render image tokens ([image XYZ]) into images.
    """

    from os import path
    from django import template
    from core import utils

    def _replace(match):
        templates = [path.join('renders', 'image')]
        tpl = template.loader.select_template(
            ["%s.html" % p for p in templates])

        return tpl.render(template.Context(
            {'image': utils.image_parse(match, model)}))

    return utils.image_sub(value, _replace)


@register.filter(is_safe=True)
@defaultfilters.stringfilter
def stripimages(value):
    """
    Remove image tokens ([image XYZ]).
    """

    from core import utils

    def _replace(match):
        return ''

    return utils.image_sub(value, _replace)


@register.filter(is_safe=True)
@defaultfilters.stringfilter
def striptokens(value):
    """
    Remove template tag tokens.
    """

    return stripimages(value)


@register.simple_tag
def gplus_publisher(publisher=None):
    from django import conf
    from django import template

    if publisher is None:
        publisher = getattr(conf.settings, 'GOOGLE_PLUS_PUBLISHER', None)

    if publisher is None:
        raise template.TemplateSyntaxError(
            'The gplus_publisher template tag requires a `publisher`. You must either pass it as an argument or set GOOGLE_PLUS_PUBLISHER in your settings.')

    return publisher
