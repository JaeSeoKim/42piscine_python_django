from typing import Any
from django import http
from django.http.response import HttpResponseBase
from ex.models.article import Article
from django.views.generic import DetailView


class Detail(DetailView):
    template_name = "detail.html"
    model = Article
