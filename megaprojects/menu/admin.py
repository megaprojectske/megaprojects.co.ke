from django.contrib import admin

from .models import Menu, Link
from .forms import LinkForm


def make_enabled(modeladmin, request, queryset):
    queryset.update(enabled=True)
make_enabled.short_description = "Mark selected menus/links as Enabled"


def make_disabled(modeladmin, request, queryset):
    queryset.update(enabled=False)
make_disabled.short_description = "Mark selected menus/links as Disabled"


class MenuLinkInline(admin.TabularInline):

    extra = 1
    fields = ['title', 'parent', 'order', 'url',
              'view_name', 'kwargs', 'enabled']
    ordering = ['parent', 'order']
    model = Link

    form = LinkForm


class MenuAdmin(admin.ModelAdmin):

    actions = [make_enabled, make_disabled]
    inlines = [MenuLinkInline]
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


class LinkLinkInline(admin.TabularInline):

    extra = 1
    fields = ['title', 'menu', 'order', 'url',
              'view_name', 'kwargs', 'enabled']
    ordering = ['parent', 'order']
    model = Link

    form = LinkForm


class LinkAdmin(admin.ModelAdmin):

    actions = [make_enabled, make_disabled]
    inlines = [LinkLinkInline]
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

    form = LinkForm


admin.site.register(Menu, MenuAdmin)
admin.site.register(Link, LinkAdmin)
