from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from locallibrary.forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})