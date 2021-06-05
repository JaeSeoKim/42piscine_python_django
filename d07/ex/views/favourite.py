from ex.forms import favourite
from ex.models.article import UserFavouriteArticle
from django.contrib.auth.mixins import LoginRequiredMixin
from ex.forms.favourite import FavouriteForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.urls import reverse_lazy


class Favourite(LoginRequiredMixin, FormView):
    form_class = FavouriteForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')

    def form_valid(self, form: AuthenticationForm):
        article_id = form.cleaned_data['article']
        try:
            UserFavouriteArticle.get(
                article=article_id, user=self.request.user).delete()
            messages.success(
                self.request, "successful Remove to favourite.")
        except UserFavouriteArticle.DoesNotExist as e:
            UserFavouriteArticle.objects.create(
                user=self.request.user,
                article=article_id,
            )
            messages.success(
                self.request, "successful Add to favourite.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful Add to favourite. Invalid information.")
        return super().form_invalid(form)
