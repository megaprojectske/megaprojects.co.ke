from django.contrib import admin
from django.utils import text

from sorl import thumbnail

from core import admin as core_admin
import forms
import models


def program_make_published(modeladmin, request, queryset):
    queryset.update(status=True)

program_make_published.short_description = 'Mark as published'


def program_make_unpublished(modeladmin, request, queryset):
    queryset.update(status=False)

program_make_unpublished.short_description = 'Mark as unpublished'


def image_mark_published(modeladmin, request, queryset):
    queryset.update(status=True)

image_mark_published.short_description = 'Mark as published'


def image_mark_unpublished(modeladmin, request, queryset):
    queryset.update(status=False)

image_mark_unpublished.short_description = 'Mark as unpublished'


class DetailInline(admin.TabularInline):

    extra = 0
    model = models.Detail


class ImageInline(core_admin.BaseImageInline):

    form = forms.ImageInlineAdminForm
    model = models.Image


class ProgramAdmin(admin.ModelAdmin):

    actions = [program_make_published, program_make_unpublished]
    inlines = [DetailInline, ImageInline]
    list_display = ['program_title', 'abbr', 'status', 'reviewed']
    list_filter = ['status', 'reviewed']
    readonly_fields = ['shortuuid', 'slug', 'code', 'created', 'changed']
    search_fields = ['title']

    form = forms.ProgramAdminForm

    fieldsets = [
        (None, {'fields': ['title', 'abbr']}),
        (None, {'fields': ['status']}),
        (None, {'fields': ['lead', 'body']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['slug', 'code', 'shortuuid', 'created', 'changed']
        }),
    ]

    def program_title(self, obj):
        return text.Truncator(obj.title).chars(50)

    program_title.short_description = 'title'


class ImageAdmin(admin.ModelAdmin):

    actions = [image_mark_published, image_mark_unpublished]
    form = forms.ImageAdminForm
    list_display = ['img_thumbnail', 'shortuuid', 'program_title', 'status',
                    'thumbnail', 'reviewed']
    list_display_links = ['shortuuid']
    list_filter = ['status', 'thumbnail', 'reviewed']
    list_select_related = True
    readonly_fields = ['shortuuid', 'program', 'created', 'changed']
    search_fields = ['shortuuid', 'program__title']

    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['program']}),
        (None, {'fields': ['status', 'thumbnail']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['shortuuid', 'created', 'changed', 'reviewed']
        }),
    ]

    def has_add_permission(self, request):
        return False

    def img_thumbnail(self, obj):
        try:
            im = thumbnail.get_thumbnail(obj.image, '75x75')
            return '<img width="%d" height="%d" src="%s">' % (im.width, im.height, im.url)
        except IOError:
            return '<img width="75" height="75" src="">'

    img_thumbnail.allow_tags = True
    img_thumbnail.short_description = ''

    def program_title(self, obj):
        return text.Truncator(obj.program.title).chars(50)

    program_title.short_description = 'program'


admin.site.register(models.Program, ProgramAdmin)
admin.site.register(models.Image, ImageAdmin)
