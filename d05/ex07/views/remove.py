from ex05.forms.remove import RemoveForm
from django import db
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from ..models import Movies


class Remove(View):
    template = 'ex07/remove.html'

    def get(self, request):
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
        except Movies.DoesNotExist as e:
            print(e)
            return HttpResponse("No data available movies")
        choices = ((movie.title, movie.title) for movie in movies)
        context = {"form": RemoveForm(choices)}
        return render(request, self.template, context)

    def post(self, request):
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
        except Movies.DoesNotExist as e:
            return redirect(request.path)
        choices = ((movie.title, movie.title) for movie in movies)
        data = RemoveForm(choices, request.POST)
        if data.is_valid():
            try:
                Movies.objects.get(title=data.cleaned_data['title']).delete()
            except db.Error as e:
                print(e)
        return redirect(request.path)
