from django.contrib import admin

from .models import Menu, Link
from .forms import LinkAdminForm


def make_enabled(modeladmin, request, queryset):
    queryset.update(enabled=True)
make_enabled.short_description = "Mark selected menus/links as Enabled"


def make_disabled(modeladmin, request, queryset):
    queryset.update(enabled=False)
make_disabled.short_description = "Mark selected menus/links as Disabled"


class LinkInline(admin.TabularInline):

    extra = 0
    fields = ['title', 'order', 'url', 'view_name', 'kwargs', 'enabled']
    model = Link
    form = LinkAdminForm


class MenuAdmin(admin.ModelAdmin):

    actions = [make_enabled, make_disabled]
    inlines = [LinkInline]
    list_display = ['title', 'slug', 'enabled']
    list_filter = ['enabled']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created', 'changed']
    search_fields = ['title', 'slug']

    fieldsets = [
        (None, {'fields': ['title', 'slug']}),
        (None, {'fields': ['enabled']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['created', 'changed']
        }),
    ]


class LinkAdmin(admin.ModelAdmin):

    actions = [make_enabled, make_disabled]
    form = LinkAdminForm
    inlines = [LinkInline]
    list_display = ['title', 'menu', 'parent',
                    'order', 'url', 'view_name', 'enabled']
    list_filter = ['enabled', 'menu']
    readonly_fields = ['created', 'changed']
    search_fields = ['title']

    fieldsets = [
        (None, {'fields': ['title', 'menu']}),
        (None, {'fields': ['parent', 'order']}),
        (None, {'fields': ['url']}),
        (None, {'fields': [('view_name', 'args', 'kwargs')]}),
        (None, {'fields': ['enabled']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['created', 'changed']
        }),
    ]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Link, LinkAdmin)
