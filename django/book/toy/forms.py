from django import forms
from django.forms import fields
from .models import usr
from .models import usrs
from.models import contact
class EmpForm(forms.ModelForm):
    class Meta:
        model=usr
        fields="__all__"

class EmpForms(forms.ModelForm):
    class Meta:
        model=usrs
        fields="__all__"





        