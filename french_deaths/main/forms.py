from django import forms
from django.forms import ModelForm
from main.models import Morir, MorirCause
from django.core.validators import RegexValidator
from django.forms.extras.widgets import SelectDateWidget

YEAR_CHOICES = (
    ('2001', 2001),
    ('2002', 2002),
    ('2003', 2003),
    ('2004', 2004),
    ('2005', 2005),
    ('2006', 2006),
    ('2007', 2007),
    ('2008', 2008)
)


SEX_CHOICES = (
    ('Males', 'Males'),
    ('Females', 'Females')
)


# class CauseForm(ModelForm):
#     class Meta:
#         CHOICES = MorirCause.objects.all()

#         model = MorirCause
#         fields = ('cause', )
#         widgets = {
#             'cause': forms.Select(choices=((cause.id, cause.cause) for cause in CHOICES))
#             }


class CauseSearchForm(forms.Form):
    # alphanumeric = RegexValidator(r'^[a-zA-Z\s]*$', 'Only alphanumeric characters are allowed.')
    # numeric = RegexValidator(r'^[2001-2008\d]*$', 'Please choose a year from 2001 to 2008.')
    cause = forms.ModelChoiceField(required=True,
                                                        queryset=MorirCause.objects.all(),
                                                        widget=forms.Select,
                                                        )

    sex = forms.ChoiceField(required=False,
                                                widget=forms.Select,
                                                choices=SEX_CHOICES
                                                )

    year = forms.ChoiceField(required=False,
                                            # validators=[numeric],
                                            widget=forms.Select,
                                            choices=YEAR_CHOICES
                                            )


class CreateCauseForm(forms.ModelForm):
    class Meta:
        model = MorirCause
