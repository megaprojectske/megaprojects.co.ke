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


class ImageInline(BaseImageInline):

    form = ImageAdminForm
    model = Image


class PostAdmin(admin.ModelAdmin):

    actions = [make_draft, make_published, make_withdrawn]
    inlines = [ImageInline]
    list_display = ['title', 'status', 'pubdate', 'author']
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
    ]


admin.site.register(Post, PostAdmin)
