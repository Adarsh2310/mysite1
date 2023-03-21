from django.shortcuts import render
from . import forms


# Create your views here.
def userRegistrationview(request):
    form = forms.UserRegistration()
    if request.method == 'POST':
        form = forms.UserRegistration(request.POST)
        if form.is_valid():
            print("form is valid")
        # print('firstname',form.cleaned_data['firstname'])
        # print('lastname',form.cleaned_data['lastname'])
        # print('salary',form.cleaned_data['salary'])
        # print('email',form.cleaned_data['email'])
    return render(request, 'templatesapp/userRegistration.html', {'form': form})


