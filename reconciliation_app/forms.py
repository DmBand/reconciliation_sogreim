from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    """ Вход пользователя """
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'input-login'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'input-login'}),
    )
