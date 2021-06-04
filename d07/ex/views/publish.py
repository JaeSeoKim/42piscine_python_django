from django.http import request
from ex.models.article import Article
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import DatabaseError
from django.shortcuts import redirect
from ..forms import PublishForm
from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy


class Publish(LoginRequiredMixin, FormView):
    template_name = "publish.html"
    form_class = PublishForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')

    def form_valid(self, form: PublishForm):
        title = form.cleaned_data['title']
        synopsis = form.cleaned_data['synopsis']
        content = form.cleaned_data['content']
        try:
            Article.objects.create(
                title=title,
                author=self.request.user,
                synopsis=synopsis,
                content=content
            )
        except DatabaseError as e:
            messages.success(
                self.request, "Unsuccessful publish. DatabaseError")
            return redirect('index')
        messages.success(self.request, "Successful publish.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful publish. Invalid information.")
        return super().form_invalid(form)
