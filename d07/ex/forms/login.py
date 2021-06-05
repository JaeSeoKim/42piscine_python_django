from typing import Any
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}),
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )
