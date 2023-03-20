from django.shortcuts import render
from . import forms


# Create your views here.
def userRegistrationview(request):
    form = forms.UserRegistration
    return render(request, 'templatesapp/userRegistration.html', {'form': form})
