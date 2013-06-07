from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage

from ckeditor.widgets import CKEditorWidget


class MyFlatpageForm(FlatpageForm):

    content = forms.CharField(widget=CKEditorWidget())


class MyFlatPageAdmin(FlatPageAdmin):

    form = MyFlatpageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)
