from ex.forms.login import LoginForm
from ..models import User
from ..forms import LoginForm
from django.views.generic import FormView
from django.urls import reverse_lazy


class Login(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form: LoginForm):
        self.request.session.flush()
        self.request.session['user'] = {
            'id': form.cleaned_data["username"]
        }
        self.request.session.modified = True
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
