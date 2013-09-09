from django import conf
from django.core import exceptions
from django.utils import encoding
from django.utils import html


class MinifyHTMLMiddleware(object):

    def __init__(self):
        if conf.settings.DEBUG:
            # On debug does not minify html
            raise exceptions.MiddlewareNotUsed

    def process_response(self, request, response):
        if response.has_header('Content-Type') and 'text/html' in response[
                'Content-Type']:
            try:
                response.content = html.strip_spaces_between_tags(
                    response.content.strip())
            except encoding.DjangoUnicodeDecodeError:
                pass

        return response
