from django import forms


class TipForm(forms.Form):
    content = forms.CharField(required=True)
