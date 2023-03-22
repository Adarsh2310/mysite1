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
        inputemail = self.cleaned_data['email']
        if inputemail.find('gmail')== -1:
            raise forms.ValidationError('the email should contain gmail')
        return inputemail

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     validator = re.match(
    #         "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
    #     validator(email)
    #     return email




