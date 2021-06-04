from django.views.generic import RedirectView
from django.urls import reverse_lazy


class Home(RedirectView):
    url = reverse_lazy('articles')
