from django.contrib import admin
from django.contrib.flatpages import admin as flatpages_admin
from django.contrib.flatpages import models

import forms


class BaseImageInline(admin.TabularInline):

    extra = 0
    fields = ['title', 'image', 'shortuuid', 'status', 'thumbnail', 'reviewed']
    ordering = ['created']
    readonly_fields = ['shortuuid']


class FlatPageAdmin(flatpages_admin.FlatPageAdmin):

    form = forms.FlatpageForm


admin.site.unregister(models.FlatPage)
admin.site.register(models.FlatPage, FlatPageAdmin)
