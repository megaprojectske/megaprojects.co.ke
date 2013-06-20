from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.flatpages.admin import FlatpageForm

from ckeditor.widgets import CKEditorWidget


class MyFlatpageForm(FlatpageForm):

    content = forms.CharField(widget=CKEditorWidget())


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
