from django import forms

class UserRegistration(forms.Form):
    firstname:forms.CharField()
    lastname:forms.CharField()
    email:forms.CharField()
    salary:forms.FloatField()