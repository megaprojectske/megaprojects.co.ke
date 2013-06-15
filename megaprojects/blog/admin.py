from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from core.admin import BaseImageAdminForm, BaseImageInline
from .models import Post, Image


def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
make_draft.short_description = "Mark selected posts as Draft"


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected posts as Published"


def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')
make_withdrawn.short_description = "Mark selected posts as Withdrawn"


class ImageAdminForm(BaseImageAdminForm):

    class Meta:
        model = Image


class ImageInline(BaseImageInline):

    form = ImageAdminForm
    model = Image


class PostAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post


class PostAdmin(admin.ModelAdmin):

    actions = [make_draft, make_published, make_withdrawn]
    inlines = [ImageInline]
    list_display = ['title', 'status', 'pubdate', 'author']
    list_filter = ['status', 'pubdate', 'author__username']
    readonly_fields = ['drupal_id', 'uuid', 'created', 'changed']
    search_fields = ['title']

    form = PostAdminForm

    fieldsets = [
        (None, {'fields': ['title', 'author']}),
        (None, {'fields': ['pubdate']}),
        (None, {'fields': ['status']}),
        (None, {'fields': ['body']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['drupal_id', 'uuid', 'created', 'changed']
        }),
    ]


admin.site.register(Post, PostAdmin)
