from typing import Any, Dict
from ex.models.article import Article
from django.views.generic import ListView


class ArticlesView(ListView):
    template_name = "articles.html"
    model = Article

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
