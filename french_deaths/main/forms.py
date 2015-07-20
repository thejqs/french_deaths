from django import forms
from django.forms import ModelForm
from main.models import Morir, MorirCause
from django.core.validators import RegexValidator


class CauseSearchForm(forms.Form):
    alphanumeric = RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphanumeric characters are allowed.')
    numeric = RegexValidator(r'^[2001-2008\s]*$', 'Please choose a year from 2001 to 2008.')
    cause = forms.CharField(required=True,
                                            validators=[alphanumeric],
                                            widget=forms.TextInput(attrs={'class': 'form-control'})
                                            )

    gender = forms.CharField(required=False,
                                            validators=[alphanumeric],
                                            widget=forms.TextInput(attrs={'class': 'form-control'})
                                            )

    year = forms.CharField(required=True,
                                            validators=[numeric],
                                            widget=forms.TextInput(attrs={'class': 'form-control'})
                                            )


class CreateCauseForm(forms.ModelForm):
    class Meta:
        model = MorirCause
