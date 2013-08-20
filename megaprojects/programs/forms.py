from django import forms

from ckeditor.widgets import CKEditorWidget

from core.forms import BaseImageAdminForm
from .models import Program, Image


class ProgramAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Program


class ImageAdminForm(BaseImageAdminForm):

    class Meta:
        model = Image
