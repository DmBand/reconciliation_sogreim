from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import ReconciliationDate


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


# class ReconcilicationForm(forms.ModelForm):
#
#     class Meta:
#         model = ReconcilicationDate
#         fields = ['date']
#         widgets = {
#             'date': forms.DateInput(attrs={'class': 'input', 'type': 'date'})
#         }
class ReconcilicationForm(forms.Form):
    date = forms.DateTimeField(
        label='Дата сверки',
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'input',
            'type': 'date',
        })
    )
