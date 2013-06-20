from django import template


register = template.Library()


@register.assignment_tag()
def load_menu(slug):
    from menu.models import Menu

    try:
        return Menu.objects.get(slug=slug).links
    except Menu.DoesNotExist:
        return None
