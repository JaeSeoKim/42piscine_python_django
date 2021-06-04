from typing import Any, Dict
from ex.models.article import Article
from django.views.generic import ListView


class Publications(ListView):
    template_name = "publications.html"
    model = Article

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
