def image_parse(match):
    """
    re Index reference for expression:

     group(1) | group(2) | group(3)
    ==========|==========|==========
     '<<<'    | *UUID    | '>>>'
              |          |
    """
    from articles.models import Image as ArticleImage
    from blog.models import Image as BlogImage
    from programs.models import Image as ProgramImage

    try:
        image = ArticleImage.objects.get(uuid=match.group(2))
    except ArticleImage.DoesNotExist:
        try:
            image = BlogImage.objects.get(uuid=match.group(2))
        except BlogImage.DoesNotExist:
            try:
                image = ProgramImage.objects.get(uuid=match.group(2))
            except ProgramImage.DoesNotExist:
                image = None

    return image


def image_sub(content, sub_callback):
    import re

    IMAGE_RE = re.compile(
        r'(<<<)([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})(>>>)')
    return IMAGE_RE.sub(sub_callback, content)


def image_render(content):
    from os.path import join
    from django import template

    def _replace(match):
        image = image_parse(match)
        templates = [join('renders', 'image')]
        tpl = template.loader.select_template(
            ["%s.html" % p for p in templates])

        return tpl.render(template.Context({'image': image}))

    return image_sub(content, _replace)


def image_remove(content):
    def _replace(match):
        return ''

    return image_sub(content, _replace)
