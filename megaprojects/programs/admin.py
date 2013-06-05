from django.contrib import admin

from .models import Program, Detail, Image


def make_published(modeladmin, request, queryset):
    queryset.update(status=True)

make_published.short_description = "Mark selected projects as Published"


def make_unpublished(modeladmin, request, queryset):
    queryset.update(status=False)

make_unpublished.short_description = "Mark selected projects as Unpublished"


class DetailInline(admin.TabularInline):

    extra = 1
    model = Detail


class ImageInline(admin.TabularInline):

    extra = 1
    fields = ['title', 'alt', 'status', 'image', 'uuid']
    model = Image
    ordering = ['created']
    readonly_fields = ['uuid']


class ProgramAdmin(admin.ModelAdmin):

    actions = [make_published, make_unpublished]
    inlines = [DetailInline, ImageInline]
    list_display = ['title', 'abbr', 'status', 'reviewed']
    list_filter = ['status']
    readonly_fields = ['uuid', 'created', 'changed']
    search_fields = ['title']

    fieldsets = [
        (None, {'fields': ['title', 'abbr']}),
        (None, {'fields': ['status']}),
        (None, {'fields': ['lead', 'body']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['uuid', 'created', 'changed']
        }),
    ]


admin.site.register(Program, ProgramAdmin)
