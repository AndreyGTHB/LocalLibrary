import datetime

from django import forms
from django.core.exceptions import ValidationError


class BookRefreshForm(forms.Form):
    errors_text = []

    renewal_date = forms.DateField(label='Return date', help_text='Enter a date between now and 4 weeks.')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        self.errors_text.clear()
        if data < datetime.date.today():
            error = 'Invalid date - renewal is past'
            self.errors_text.append(error)
            raise ValidationError(error)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            error = 'Invalid date - renewal more than 4 weeks ahead'
            self.errors_text.append(error)
            raise ValidationError(error)
        return data
