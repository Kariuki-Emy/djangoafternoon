from django import forms
from djangoAfternoon.model import Students

class EmpForm(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"