from django import forms
from django.core.exceptions import ValidationError
import re


class RegistrationForm(forms.Form):
    errors_text = set()

    first_name = forms.CharField(label='First name:', min_length=2, max_length=20)
    last_name = forms.CharField(label='Last name:', min_length=2, max_length=20)

    username = forms.CharField(label='Username', min_length=6, max_length=25)
    email = forms.CharField(label='Email', min_length=5, max_length=30)
    password = forms.CharField(label='Password', min_length=8, max_length=30)

    def clean_email(self):
        data = self.cleaned_data['email']
        searched = re.findall(r'@\w+.\w+', data)
        if len(searched) != 1:
            error = 'Email does not correct. It have to have a domain.'
            self.errors_text.add(error)
            raise ValidationError(error)
        return data


