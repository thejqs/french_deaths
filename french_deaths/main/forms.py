from django import forms
from django.forms import ModelForm
from main.models import Morir, MorirCause
from django.core.validators import RegexValidator


class CauseSearchForm(forms.Form):
    alphanumeric = RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphanumeric characters are allowed.')
    cause = forms.CharField(required=False,
                                            initial='Tuberculosis',
                                            validators=[alphanumeric],
                                            widget=forms.TextInput(attrs={'class': 'form-control'})
                                            )

    gender = forms.CharField(required=False,
                                            validators=[alphanumeric],
                                            widget=forms.TextInput(attrs={'class': 'form-control'})
                                            )


class CreateCauseForm(forms.ModelForm):
    class Meta:
        model = MorirCause