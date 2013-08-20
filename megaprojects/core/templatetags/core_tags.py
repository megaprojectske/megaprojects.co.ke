from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def loadimages(value, model):
    """
    Convert or render image tokens ([image XYZ]) into images.
    """

    from os.path import join
    from django import template
    from core import util

    def _replace(match):
        templates = [join('renders', 'image')]
        tpl = template.loader.select_template(
            ["%s.html" % p for p in templates])
        return tpl.render(template.Context({'image': util.image_parse(match, model)}))

    return util.image_sub(value, _replace)


@register.filter(is_safe=True)
@stringfilter
def stripimages(value):
    """
    Remove image tokens ([image XYZ]).
    """

    from core import util

    def _replace(match):
        return ''

    return util.image_sub(value, _replace)


@register.filter(is_safe=True)
@stringfilter
def loadarticles(value):
    """
    Convert or render article tokens ([article XYZ]) into articles.
    """

    from os.path import join
    from django import template
    from core import util

    def _replace(match):
        templates = [join('renders', 'article')]
        tpl = template.loader.select_template(
            ["%s.html" % p for p in templates])
        return tpl.render(template.Context({'article': util.article_parse(match)}))

    return util.article_sub(value, _replace)


@register.filter(is_safe=True)
@stringfilter
def striparticles(value):
    """
    Remove article tokens ([article XYZ]).
    """

    from core import util

    def _replace(match):
        return ''

    return util.article_sub(value, _replace)


@register.filter(is_safe=True)
@stringfilter
def striptokens(value):
    """
    Remove template tag tokens.
    """

    return stripimages(striparticles(value))


@register.simple_tag
def gplus_publisher(publisher=None):
    from django.conf import settings
    from django.template import TemplateSyntaxError

    if publisher is None:
        publisher = getattr(settings, 'GOOGLE_PLUS_PUBLISHER', None)

    if publisher is None:
        raise TemplateSyntaxError(
            'The gplus_publisher template tag requires a `publisher`. You must either pass it as an argument or set GOOGLE_PLUS_PUBLISHER in your settings.')

    return publisher
