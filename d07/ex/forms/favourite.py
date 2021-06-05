from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.forms.widgets import HiddenInput


class FavouriteForm(forms.Form):
    article = forms.IntegerField(widget=HiddenInput(), required=True)

    def __init__(self, article, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if article is not None:
            self.fields['article'].initial = article
