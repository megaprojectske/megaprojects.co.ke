from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def render_images(value, model):
    from os.path import join
    from django import template
    from core import util

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
    from core import util

    def _replace(match):
        return ''

    return util.image_sub(value, _replace)


# See: https://github.com/lettertwo/django-socialsharing
@register.inclusion_tag('social/addthis/addthis_js.html', takes_context=True)
def addthis_js(context, pubid=None, share_url=None, ga_tracker=None, ga_social=True, track_clickback=True, track_addressbar=True):
    from django.conf import settings
    from django.template import TemplateSyntaxError

    """
    addthis
    =======
    The addthis templatetag will insert the necessary scripts to make use of
    the [AddThis](http://www.addthis.com) widget.

    Basic usage:
    ------------

        {% addthis_js pubid=xxxxxxxxxx %}

    or with `ADDTHIS_PUBID` defined in settings.py:

        {% addthis_js %}

    The only required argument is `pubid`. You may optionally provide a global
    setting for this by adding `ADDTHIS_PUBID = xxxxxx` to your settings.py.
    Setting this value means that you can omit the `pubid` argument when
    invoking the templatetag.

    Optional settings:
    ------------------
    `share_url`: The url to share. Pass this argument to override the default
    AddThis value (the URL of the page being viewed). Example:

        {% addthis_js 'http://myurl.com' %}

    `track_clickback`: From the AddThis docs:

        Set to true to allow us to append a variable to your URLs upon sharing.
        We'll use this to track how many people come back to your content via
        links shared with AddThis. Highly recommended.

    default value is `True`.
    **Note:** You may optionally set
    `ADDDTHIS_TRACK_CLICKBACK = False` to always force this value to `False`.

    To enable tracking via Google Analytics:
    ----------------------------------------
    * add `ADDTHIS_GA_TRACKING_ENABLED = True` to your settings.py
    * add `ADDTHIS_GA_TRACKER = UA-XXXXXX-X` to your settings.py

    **Note:** If you don't set `ADDDTHIS_GA_TRACKER`, the template tag will
    attempt to fall back to `GOOGLE_ANALYTICS_PROPERTY_ID` (which is used by
    [django-analytical](http://github.com/jcassee/django-analytical)).
    """

    if getattr(settings, 'ADDTHIS_GA_TRACKING_ENABLED', False):
        if ga_tracker is None:
            ga_tracker = getattr(settings, 'ADDTHIS_GA_TRACKER', getattr(
                settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', None))
        if ga_tracker is None:
            raise TemplateSyntaxError(
                'The addthis template tag is configured to use Google Analytics, but a tracking code was not found. You must either pass it as an argument or set ADDTHIS_GA_TRACKER in settings.py')

    if pubid is None:
        pubid = getattr(settings, 'ADDTHIS_PUB_ID', None)
    if pubid is None:
        raise TemplateSyntaxError(
            'The addthis template tag requires a pubid. You must either pass it as an argument or set ADDTHIS_PUB_ID in settings.py.')

    return {
        'data_ga_property': ga_tracker,
        'data_ga_social': ga_social,
        'data_track_addressbar': track_addressbar,
        'data_track_clickback': track_clickback,
        'pubid': pubid,
        'share_url': share_url,
    }


@register.inclusion_tag('social/intensedebate/intensedebate_js.html', takes_context=True)
def intensedebate_js(context, post_id=None, post_url=None, post_id_prefix='', post_id_suffix=''):
    from django.conf import settings
    from django.template import TemplateSyntaxError

    intensedebate_acct = getattr(settings, 'INTENSEDEBATE_ACCT', None)
    if intensedebate_acct is None:
        raise TemplateSyntaxError(
            'The intensedebate template tag requires an account. You must set INTENSEDEBATE_ACCT in settings.py.')

    if post_id is None:
        raise TemplateSyntaxError(
            'The intensedebate template tag requires a post ID. You must pass post_id as an argument.')

    return {
        'account': intensedebate_acct,
        'post_id': "%s%s%s" % (post_id_prefix, post_id, post_id_suffix),
        'post_url': post_url,
    }
