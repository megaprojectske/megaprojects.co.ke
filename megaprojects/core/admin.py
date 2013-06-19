from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.core.files.images import get_image_dimensions

from ckeditor.widgets import CKEditorWidget


class BaseImageAdminForm(forms.ModelForm):

    def clean_image(self):
        image = self.cleaned_data['image']

        try:
            w, h = get_image_dimensions(image)
        except TypeError:
            pass
        else:
            if w > 1280:
                raise forms.ValidationError(
                    "The image is %i pixels wide. It's supposed to be <= 1280 pixels wide." % w)

        return image


class BaseImageInline(admin.TabularInline):

    extra = 1
    fields = ['title', 'image', 'uuid', 'shortuuid', 'status', 'thumbnail', 'reviewed']
    ordering = ['created']
    readonly_fields = ['uuid', 'shortuuid']


class MyFlatpageForm(FlatpageForm):

    content = forms.CharField(widget=CKEditorWidget())


class MyFlatPageAdmin(FlatPageAdmin):

    form = MyFlatpageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)
