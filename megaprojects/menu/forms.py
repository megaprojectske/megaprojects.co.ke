from django import forms
from django.conf import settings

from .models import Link


# See: from django.contrib.flatpages.forms.FlatpageForm
class LinkForm(forms.ModelForm):

    url = forms.RegexField(
        label='URL', max_length=255, regex=r'^[-\w/\.~]+$', required=False, help_text='Example: "/about/contact/". Make sure to have leading and trailing slashes.',
        error_message='This value must contain only letters, numbers, dots, underscores, dashes, slashes or tildes.')
    view_name = forms.CharField(
        label='View name', max_length=255, required=False)

    def clean_url(self):
        url = self.cleaned_data['url']

        if url:
            if not url.startswith('/'):
                raise forms.ValidationError('URL is missing a leading slash.')
            if (settings.APPEND_SLASH and 'django.middleware.common.CommonMiddleware' in settings.MIDDLEWARE_CLASSES and not url.endswith('/')):
                raise forms.ValidationError('URL is missing a trailing slash.')

        return url

    class Meta:
        model = Link
