from django.contrib import admin

from core.admin import BaseImageInline
from .models import Post, Image
from .forms import PostAdminForm, ImageAdminForm


def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
make_draft.short_description = "Mark selected posts as Draft"


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected posts as Published"


def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')
make_withdrawn.short_description = "Mark selected posts as Withdrawn"


def make_comments_enabled(modeladmin, request, queryset):
    queryset.update(enable_comments=True)
make_comments_enabled.short_description = "Mark selected posts with Comments Enabled"


def make_comments_disabled(modeladmin, request, queryset):
    queryset.update(enable_comments=False)
make_comments_disabled.short_description = "Mark selected posts with Comments Disabled"


class ImageInline(BaseImageInline):

    form = ImageAdminForm
    model = Image


class PostAdmin(admin.ModelAdmin):

    actions = [make_draft, make_published, make_withdrawn,
               make_comments_enabled, make_comments_disabled]
    inlines = [ImageInline]
    list_display = ['title', 'status', 'pubdate',
                    'author', 'enable_comments', 'reviewed']
    list_filter = ['status', 'pubdate', 'author__username']
    readonly_fields = [
        'drupal_id', 'shortuuid', 'slug', 'code', 'created', 'changed']
    search_fields = ['title']

    form = PostAdminForm

    fieldsets = [
        (None, {'fields': ['title', 'author']}),
        (None, {'fields': ['pubdate']}),
        (None, {'fields': ['status']}),
        (None, {'fields': ['body']}),
        (None, {'fields': ['slug', 'code']}),
        ('Advanced', {
            'classes': ['collapse'],
            'fields': ['enable_comments', 'drupal_id', 'shortuuid', 'created', 'changed']
        }),
        (None, {'fields': ['reviewed']}),
    ]


admin.site.register(Post, PostAdmin)
