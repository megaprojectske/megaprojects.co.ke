from django import forms
from django.contrib.flatpages import admin
from django.core.files import images

from ckeditor import widgets


class FlatpageForm(admin.FlatpageForm):

    content = forms.CharField(widget=widgets.CKEditorWidget())


class BaseImageAdminForm(forms.ModelForm):

    def clean_image(self):
        image = self.cleaned_data['image']

        try:
            w, h = images.get_image_dimensions(image)
        except TypeError:
            pass
        else:
            if w > 1280:
                raise forms.ValidationError(
                    "The image is %i pixels wide. It's should to be <= 1280 pixels wide." % w)

        return image
