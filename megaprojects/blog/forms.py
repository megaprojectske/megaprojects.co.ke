from django import forms

from ckeditor.widgets import CKEditorWidget

from core.forms import BaseImageAdminForm
from .models import Post, Image


class PostAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post


class ImageAdminForm(BaseImageAdminForm):

    class Meta:
        model = Image
