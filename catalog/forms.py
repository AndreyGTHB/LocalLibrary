from django import forms
from django.core.exceptions import ValidationError


class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=30)

    def clean_name(self):
        data = self.cleaned_data['name']

        if len(data) < 2:
            raise ValidationError('Name length have to be 2 at least')

        return data
