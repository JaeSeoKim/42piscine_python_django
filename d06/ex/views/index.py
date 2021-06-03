import uuid
from django.views.generic import TemplateView
from django.shortcuts import render


class Index(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)
