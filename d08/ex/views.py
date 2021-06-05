from django.http.response import HttpResponse
from ex.models import Image
from ex.forms import ImageForm
from django.views.generic import FormView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy


class Index(ListView, FormView):
    success_url = reverse_lazy('index')
    template_name = 'index.html'
    form_class = ImageForm
    model = Image
    queryset = model.objects.all().order_by('-id')

    def form_valid(self, form: ImageForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form: ImageForm) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)
