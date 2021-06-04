from ex.forms.tip import DeleteTipForm, VoteForm
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
    http_method_names = ['post', 'put', 'delete']
    login_url = reverse_lazy('login')

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(Tip, self).dispatch(*args, **kwargs)

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

    def __error_msg(self, msg):
        messages.error(
            self.request, f"Unsuccessful delete Tip. ({msg})")
        return redirect('index')

    def delete(self, request):
        form = DeleteTipForm(None, request.POST)
        if not form.is_valid():
            return self.__error_msg("Invaild form data.")
        try:
            tip: TipModel = TipModel.objects.get(
                id=form.cleaned_data['id'])
            if tip.author != request.user:
                return self.__error_msg("access denied")
            tip.delete()
            messages.success(self.request, "Successful delete Tip.")
        except TipModel.DoesNotExist as e:
            return self.__error_msg("Tip does not exist")
        except DatabaseError as e:
            return self.__error_msg("db error")

        return redirect('index')

    def put(self, request):
        form = VoteForm(None, request.POST)
        if not form.is_valid():
            return self.__error_msg("Invaild form data.")
        try:
            tip: TipModel = TipModel.objects.get(id=form.cleaned_data['id'])
            if form.cleaned_data['type']:
                tip.upvote(request.user)
            else:
                tip.downvote(request.user)
        except TipModel.DoesNotExist as e:
            return self.__error_msg("Tip does not exist")
        except DatabaseError as e:
            return self.__error_msg("db error")
        messages.success(request, 'Voted success!')
        return redirect('index')
