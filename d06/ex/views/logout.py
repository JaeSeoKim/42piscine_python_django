from django.contrib.auth import logout
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class Logout(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('index')
