from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import ReconciliationDate


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'input-login'}
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'input-login'}
    ))
