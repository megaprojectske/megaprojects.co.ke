from django import template


register = template.Library()


@register.assignment_tag()
def loadarticles(count):
    from articles.models import Article

    return Article.objects.published()[:count]
