from django import template
from django.template.defaultfilters import stringfilter

from core import util

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def render_images(value, model):
    from os.path import join
    from django import template

    def _replace(match):
        templates = [join('renders', 'image')]
        tpl = template.loader.select_template(
            ["%s.html" % p for p in templates])
        return tpl.render(template.Context({
            'image': util.image_parse(match, model)
        }))

    return util.image_sub(value, _replace)


@register.filter(is_safe=True)
@stringfilter
def remove_images(value):
    def _replace(match):
        return ''

    return util.image_sub(value, _replace)
