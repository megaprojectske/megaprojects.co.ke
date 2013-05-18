from django.contrib import admin

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


class ImageInline(admin.TabularInline):

    extra = 1
    fields = ['title', 'alt', 'status', 'image', 'uuid']
    model = Image
    ordering = ['created']
    readonly_fields = ['uuid']


class PostAdmin(admin.ModelAdmin):

    actions = [make_draft, make_published, make_withdrawn]
    inlines = [ImageInline]
    list_display = ['title', 'status', 'pubdate', 'author']
    list_filter = ['status', 'pubdate', 'author__username']
    readonly_fields = ['drupal_id', 'uuid', 'created', 'changed']
    search_fields = ['title']

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
