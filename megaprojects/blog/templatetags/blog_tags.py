from django import template


register = template.Library()


@register.assignment_tag()
def loadposts(count):
    from blog.models import Post

    return Post.objects.published()[:count]
