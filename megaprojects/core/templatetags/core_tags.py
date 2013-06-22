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


@register.filter(is_safe=True)
@stringfilter
def render_articles(value):
    from os.path import join
    from django import template
    from core import util

    def _replace(match):
        templates = [join('renders', 'article')]
        tpl = template.loader.select_template(
            ["%s.html" % p for p in templates])
        return tpl.render(template.Context({
            'article': util.article_parse(match)
        }))

    return util.article_sub(value, _replace)


@register.filter(is_safe=True)
@stringfilter
def remove_articles(value):
    from core import util

    def _replace(match):
        return ''

    return util.article_sub(value, _replace)


# See: https://github.com/lettertwo/django-socialsharing
@register.inclusion_tag('external/addthis/config_js.html')
def addthis_config(data_ga_social=True, track_clickback=True, track_addressbar=True, ui_use_css=True, twitter_bitly=True, twitter_via=None):
    """
    Inserts the necessary scripts to make use of the
    [AddThis](http://www.addthis.com) widget.

    Sample usage::

        {% addthis_js %}

    The only required argument is a global setting ``ADDTHIS_PUBID = xxxxxx``
    added to your settings.py.

    Optional arguments::

        {% addthis_js [data_ga_social] [track_clickback] [track_addressbar] [ui_use_css] [twitter_bitly] [twitter_via] %}

    ``share_url``: The url to share. Pass this argument to override the default
    AddThis value (the URL of the page being viewed). Example::

        {% addthis_js 'http://myurl.com' %}

    ``track_clickback`` (default = True): From the AddThis docs:

        Set to true to allow us to append a variable to your URLs upon sharing.
        We'll use this to track how many people come back to your content via
        links shared with AddThis. Highly recommended.

    ``track_addressbar`` (default = True): TODO: Add doc

    ``twitter_via`` (default = None): TODO: Add doc

    ``shorten_bitly`` (default = None): TODO: Add doc

    **Note:** You may optionally set ``ADDDTHIS_TRACK_CLICKBACK = False`` to
    always force this value to ``False``.

    To enable tracking via Google Analytics:

    * add ``ADDTHIS_GA_TRACKING_ENABLED = True`` to your settings.py
    * add ``ADDTHIS_GA_TRACKER = UA-XXXXXX-X`` to your settings.py

    **Note:** If you don't set ``ADDTHIS_DATA_GA_PROPERTY``, the template tag will
    attempt to fall back to ``GOOGLE_ANALYTICS_PROPERTY_ID``.
    """

    from django.conf import settings
    from django.template import TemplateSyntaxError

    if getattr(settings, 'ADDTHIS_GA_TRACKING_ENABLED', False):
        data_ga_property = getattr(settings, 'ADDTHIS_DATA_GA_PROPERTY', getattr(
            settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', None))
        if data_ga_property is None:
            raise TemplateSyntaxError(
                'The addthis template tag is configured to use Google Analytics, but a tracking code was not found. You must set ADDTHIS_DATA_GA_PROPERTY in settings.py')
    else:
        data_ga_property = None

    return {
        'data_ga_property': data_ga_property,
        'data_ga_social': data_ga_social,
        'data_track_addressbar': track_addressbar,
        'data_track_clickback': track_clickback,
        'twitter_bitly': twitter_bitly,
        'twitter_via': twitter_via,
        'ui_use_css': ui_use_css,
    }


@register.inclusion_tag('external/addthis/widget_js.html')
def addthis_widget():
    from django.conf import settings
    from django.template import TemplateSyntaxError

    pubid = getattr(settings, 'ADDTHIS_PUB_ID', None)
    if pubid is None:
        raise TemplateSyntaxError(
            'The addthis template tag requires a pubid. You must either pass it as an argument or set ADDTHIS_PUB_ID in settings.py.')

    return {
        'pubid': pubid,
    }


@register.inclusion_tag('external/intensedebate/config_js.html')
def intensedebate_config(post_id=None, post_url=None, post_id_prefix='', post_id_suffix=''):
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
        'idcomments_acct': intensedebate_acct,
        'idcomments_post_id': "%s%s%s" % (post_id_prefix, post_id, post_id_suffix),
        'idcomments_post_url': post_url,
    }


@register.inclusion_tag('external/intensedebate/load_wrapper_js.html')
def intensedebate_cw():
    return


@register.inclusion_tag('external/intensedebate/link_wrapper_js.html')
def intensedebate_lw():
    return


@register.inclusion_tag('external/google_analytics/analytics_js.html')
def analytics_load():
    from django.conf import settings
    from django.template import TemplateSyntaxError

    tracking_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', None)
    site_domain = getattr(settings, 'GOOGLE_ANALYTICS_SITE_DOMAIN', None)

    if tracking_id is None or site_domain is None:
        raise TemplateSyntaxError(
            'The analytics template tag requires a tracking ID and site domain. You must set GOOGLE_ANALYTICS_PROPERTY_ID and GOOGLE_ANALYTICS_SITE_DOMAIN in settings.py.')

    return {
        'tracking_id': tracking_id,
        'site_domain': site_domain,
    }
