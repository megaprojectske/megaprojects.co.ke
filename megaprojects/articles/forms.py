from django import forms

from ckeditor.widgets import CKEditorWidget

from core.forms import BaseImageAdminForm
from .models import Article, Image


class ArticleAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article


class ImageAdminForm(BaseImageAdminForm):

    class Meta:
        model = Image
