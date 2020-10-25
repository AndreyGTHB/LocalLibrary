from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=20)
    login = forms.CharField(label='Login', max_length=25)
    email = forms.CharField(label='Email', max_length=30)
    password = forms.CharField(label='Password', max_length=30)
