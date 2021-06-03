from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import DatabaseError
from ..forms import TipForm
from ..models import TipModel


class Tip(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def post(self, request):
        form = TipForm(request.POST)
        if form.is_valid():
            try:
                TipModel.objects.create(
                    content=form.cleaned_data['content'],
                    author=self.request.user
                )
                messages.success(self.request, "Successful create Tip.")
            except DatabaseError as e:
                messages.error(
                    self.request, "Unsuccessful create Tip. (db error)")
        else:
            messages.error(
                self.request, "Unsuccessful create Tip. (Invalid form data.)")
        return redirect('index')
