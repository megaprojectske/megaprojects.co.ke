from django import forms

from ckeditor import widgets

from core import forms as core_forms
import models


class ProgramAdminForm(forms.ModelForm):

    title = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '3', 'maxlength': '255', 'class': 'vLargeTextField'}))
    lead = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows': '3', 'maxlength': '255', 'class': 'vLargeTextField'}))
    body = forms.CharField(required=False, widget=widgets.CKEditorWidget())

    class Meta:
        model = models.Program


class ImageInlineAdminForm(core_forms.BaseImageAdminForm):

    title = forms.CharField(label='title', widget=forms.Textarea(
        attrs={'rows': '3', 'class': 'vTextField'}))

    class Meta:
        model = models.Image


class ImageAdminForm(core_forms.BaseImageAdminForm):

    title = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '3', 'maxlength': '255', 'class': 'vLargeTextField'}))

    class Meta:
        model = models.Image
