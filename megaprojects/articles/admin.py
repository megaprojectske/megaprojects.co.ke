from django.contrib import admin
from django.utils import text

from sorl import thumbnail
from sorl.thumbnail.helpers import ThumbnailError

from core import admin as core_admin
import forms
import models


def article_mark_draft(modeladmin, request, queryset):
    queryset.update(status=models.Article.STATUS_DRAFT)
article_mark_draft.short_description = 'Mark as draft'


def article_mark_published(modeladmin, request, queryset):
    queryset.update(status=models.Article.STATUS_PUBLISHED)
article_mark_published.short_description = 'Mark as published'


def article_mark_withdrawn(modeladmin, request, queryset):
    queryset.update(status=models.Article.STATUS_WITHDRAWN)
article_mark_withdrawn.short_description = 'Mark as withdrawn'


def article_enable_comments(modeladmin, request, queryset):
    queryset.update(enable_comments=True)
article_enable_comments.short_description = 'Enable comments'


def article_disable_comments(modeladmin, request, queryset):
    queryset.update(enable_comments=False)
article_disable_comments.short_description = 'Disable comments'


def image_mark_published(modeladmin, request, queryset):
    queryset.update(status=True)
image_mark_published.short_description = 'Mark as published'


def image_mark_unpublished(modeladmin, request, queryset):
    queryset.update(status=False)
image_mark_unpublished.short_description = 'Mark as unpublished'


class ImageInline(core_admin.BaseImageInline):

    form = forms.ImageInlineAdminForm
    model = models.Image


class ArticleAdmin(admin.ModelAdmin):

    actions = [article_mark_draft, article_mark_published,
               article_mark_withdrawn, article_enable_comments,
               article_disable_comments]
    form = forms.ArticleAdminForm
    inlines = [ImageInline]
    list_display = ['article_title', 'pubdate', 'program_abbr', 'author',
                    'kind', 'status', 'comments', 'reviewed']
    list_filter = ['pubdate', 'status', 'kind', 'enable_comments', 'reviewed',
                   'author', 'program']
    readonly_fields = ['shortuuid', 'slug', 'code', 'created', 'changed']
    search_fields = ['title']
    list_select_related = True

    fieldsets = [
        (None, {'fields': ['title', 'pubdate']}),
        (None, {'fields': ['program']}),
        (None, {'fields': ['author', 'kind', 'status']}),
        (None, {'fields': ['lead', 'body', 'enable_comments']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['slug', 'code', 'shortuuid', 'created', 'changed',
                       'reviewed']
        }),
    ]

    def article_title(self, obj):
        return text.Truncator(obj.title).chars(50)

    article_title.short_description = 'title'

    def program_abbr(self, obj):
        return obj.program.abbr if obj.program else None

    program_abbr.short_description = 'program'

    def comments(self, obj):
        return obj.enable_comments

    comments.boolean = True


class ImageAdmin(admin.ModelAdmin):

    actions = [image_mark_published, image_mark_unpublished]
    form = forms.ImageAdminForm
    list_display = ['img_thumbnail', 'shortuuid', 'article_title', 'status',
                    'thumbnail', 'reviewed']
    list_display_links = ['shortuuid']
    list_filter = ['status', 'thumbnail', 'reviewed']
    list_select_related = True
    readonly_fields = ['shortuuid', 'image', 'article', 'thumbnail', 'created',
                       'changed']
    search_fields = ['shortuuid', 'article__title']

    fieldsets = [
        (None, {'fields': ['title', 'image']}),
        (None, {'fields': ['article']}),
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
        except (ThumbnailError, IOError):
            return '<img width="75" height="75" src="">'

    img_thumbnail.allow_tags = True
    img_thumbnail.short_description = ''

    def article_title(self, obj):
        return text.Truncator(obj.article.title).chars(50)

    article_title.short_description = 'article'


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Image, ImageAdmin)
