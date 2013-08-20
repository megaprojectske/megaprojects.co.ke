from django import template


register = template.Library()


@register.assignment_tag()
def loadprograms(count, order=None):
    from programs.models import Program

    if order:
        return Program.objects.published().order_by(order)[:count]

    return Program.objects.published()[:count]
