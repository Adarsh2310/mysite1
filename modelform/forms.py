from django import forms
from modelform.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'
