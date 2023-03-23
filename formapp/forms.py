from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


class UserRegistration(forms.Form):
    GENDER = [('male', 'MALE'), ('female', 'FEMALE')]
    firstname = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(10)])
    lastname = forms.CharField()
    email = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    salary = forms.FloatField()
    password = forms.CharField(widget=forms.PasswordInput)

    # validation of the method

    def clean_email(self):
        se = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        inputemail = self.cleaned_data['email']
        if re.fullmatch(se,inputemail):
            print('valid mail')
        else:
            raise forms.ValidationError('invalid')
        return inputemail
