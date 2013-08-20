from django.contrib import admin

from core.admin import BaseImageInline
from .models import Article, Image
from .forms import ArticleAdminForm, ImageAdminForm


def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')

make_draft.short_description = 'Mark selected articles as Draft'


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

make_published.short_description = 'Mark selected articles as Published'


def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')

make_withdrawn.short_description = 'Mark selected articles as Withdrawn'


def make_comments_enabled(modeladmin, request, queryset):
    queryset.update(enable_comments=True)

make_comments_enabled.short_description = 'Mark selected articles with Comments Enabled'


def make_comments_disabled(modeladmin, request, queryset):
    queryset.update(enable_comments=False)

make_comments_disabled.short_description = 'Mark selected articles with Comments Disabled'


class ImageInline(BaseImageInline):

    form = ImageAdminForm
    model = Image


class ArticleAdmin(admin.ModelAdmin):

    actions = [make_draft, make_published, make_withdrawn,
               make_comments_enabled, make_comments_disabled]
    form = ArticleAdminForm
    inlines = [ImageInline]
    list_display = ['title', 'status', 'pubdate',
                    'program_abbr', 'author', 'enable_comments', 'reviewed']
    list_filter = ['status', 'pubdate', 'program', 'author__username']
    readonly_fields = [
        'drupal_id', 'shortuuid', 'slug', 'code', 'created', 'changed']
    search_fields = ['title']

    fieldsets = [
        (None, {'fields': ['title', 'author', 'kind']}),
        (None, {'fields': ['pubdate']}),
        (None, {'fields': ['status', 'program']}),
        (None, {'fields': ['lead', 'body']}),
        (None, {'fields': ['slug', 'code']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['enable_comments', 'drupal_id', 'shortuuid', 'created', 'changed']
        }),
        (None, {'fields': ['reviewed']}),
    ]

    def program_abbr(self, obj):
        return obj.program.abbr if obj.program else None

    program_abbr.short_description = 'Program'


admin.site.register(Article, ArticleAdmin)
