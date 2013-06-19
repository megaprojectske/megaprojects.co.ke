from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from core.admin import BaseImageAdminForm, BaseImageInline
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


class ImageAdminForm(BaseImageAdminForm):

    class Meta:
        model = Image


class ImageInline(BaseImageInline):

    form = ImageAdminForm
    model = Image


class ProgramAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Program


class ProgramAdmin(admin.ModelAdmin):

    actions = [make_published, make_unpublished]
    inlines = [DetailInline, ImageInline]
    list_display = ['title', 'abbr', 'status', 'reviewed']
    list_filter = ['status']
    readonly_fields = ['shortuuid', 'slug', 'code', 'created', 'changed']
    search_fields = ['title']

    form = ProgramAdminForm

    fieldsets = [
        (None, {'fields': ['title', 'abbr']}),
        (None, {'fields': ['status']}),
        (None, {'fields': ['lead', 'body']}),
        (None, {'fields': ['slug', 'code']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['shortuuid', 'created', 'changed']
        }),
    ]


admin.site.register(Program, ProgramAdmin)
