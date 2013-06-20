from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from core.admin import BaseImageAdminForm, BaseImageInline
from .models import Article, Image


def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
make_draft.short_description = "Mark selected articles as Draft"


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected articles as Published"


def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')
make_withdrawn.short_description = "Mark selected articles as Withdrawn"


class ImageAdminForm(BaseImageAdminForm):

    class Meta:
        model = Image


class ImageInline(BaseImageInline):

    form = ImageAdminForm
    model = Image


class ArticleAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article


class ArticleAdmin(admin.ModelAdmin):

    actions = [make_draft, make_published, make_withdrawn]
    inlines = [ImageInline]
    list_display = ['title', 'status', 'pubdate',
                    'program_abbr', 'author', 'reviewed']
    list_filter = ['status', 'pubdate', 'program', 'author__username']
    readonly_fields = [
        'drupal_id', 'uuid', 'shortuuid', 'slug', 'code', 'created', 'changed']
    search_fields = ['title']

    form = ArticleAdminForm

    fieldsets = [
        (None, {'fields': ['title', 'author', 'kind']}),
        (None, {'fields': ['pubdate']}),
        (None, {'fields': ['status', 'program']}),
        (None, {'fields': ['lead', 'body']}),
        (None, {'fields': ['slug', 'code']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['enable_comments', 'drupal_id', 'uuid', 'shortuuid', 'created', 'changed']
        }),
        (None, {'fields': ['reviewed']}),
    ]

    def program_abbr(self, obj):
        return obj.program.abbr if obj.program else None
    program_abbr.short_description = 'Program'


admin.site.register(Article, ArticleAdmin)
