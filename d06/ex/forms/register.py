from ..models import User
from django import forms


class RegiserForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=32, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, min_length=8, max_length=256, required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, min_length=8, max_length=256, required=True)

    def clean(self):
        super(RegiserForm,)
        data = self.cleaned_data

        username = data.get("username")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            self.add_error('password', 'Passwords did not match')
            self.add_error('confirm_password', 'Passwords did not match')

        if User.objects.filter(username=username).exists():
            self.add_error('username', "Already exist user name")

        return self.cleaned_data
