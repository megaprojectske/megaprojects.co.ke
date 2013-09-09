from django import template


register = template.Library()


@register.assignment_tag()
def loadarticles(count, program=None, kind=None):
    from articles import models

    article_list = models.Article.objects.published()

    if program:
        article_list = article_list.filter(program=program)

    if kind:
        article_list = article_list.filter(kind=kind)

    return article_list[:count]
