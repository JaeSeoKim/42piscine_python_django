from django import forms
from django.forms.widgets import Textarea


class PublishForm(forms.Form):
    title = forms.CharField(max_length=64, required=True)
    synopsis = forms.CharField(max_length=312, required=True)
    content = forms.CharField(widget=Textarea(), required=True)
