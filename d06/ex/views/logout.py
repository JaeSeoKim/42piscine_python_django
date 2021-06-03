from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect


class Logout(View):
    template_name = "index.html"

    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('index')
