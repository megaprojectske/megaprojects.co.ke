from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from .forms import MyFlatpageForm


class BaseImageInline(admin.TabularInline):

    extra = 1
    fields = ['title', 'image', 'shortuuid', 'status', 'thumbnail', 'reviewed']
    ordering = ['created']
    readonly_fields = ['shortuuid']


class MyFlatPageAdmin(FlatPageAdmin):

    form = MyFlatpageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)
