from django import template
from django.template.defaultfilters import stringfilter

from core import util

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def render_images(content):
    return util.image_render(content)


@register.filter(is_safe=True)
@stringfilter
def remove_images(content):
    return util.image_remove(content)
