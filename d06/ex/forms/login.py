from ..models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=32, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, min_length=8, max_length=256, required=True)

    def clean(self):
        super(LoginForm,)
        data = self.cleaned_data

        username = data.get("username")
        password = data.get("password")

        try:
            user: User = User.objects.get(username=username)
        except User.DoesNotExist as e:
            self.add_error('username', 'user does not exist')
            self.add_error('password', 'user does not exist')
            return self.cleaned_data

        if not user.check_password(password):
            self.add_error('password', 'Wrong password')

        return self.cleaned_data
