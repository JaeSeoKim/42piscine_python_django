from typing import Any
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from ..forms import RegisterForm
from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy


class Register(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            messages.error(self.request, 'You already logined!')
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: RegisterForm):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful registration. Invalid information.")
        return super().form_invalid(form)
