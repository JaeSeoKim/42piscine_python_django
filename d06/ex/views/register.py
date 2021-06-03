from ..models import User
from ..forms import RegiserForm
from django.views.generic import FormView
from django.urls import reverse_lazy


class Register(FormView):
    template_name = "register.html"
    form_class = RegiserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form: RegiserForm):
        new_user = User()
        new_user.username = form.cleaned_data['username']
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
