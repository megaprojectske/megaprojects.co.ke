from django import template


register = template.Library()


@register.assignment_tag()
def loadarticles(count, program=None):
    from articles.models import Article

    if program:
        return Article.objects.published().filter(program=program)[:count]

    return Article.objects.published()[:count]
