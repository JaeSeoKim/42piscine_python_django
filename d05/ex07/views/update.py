from django import db
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from ..models import Movies
from ..forms import UpdateForm


class Update(View):
    template = 'ex07/update.html'

    def get(self, request):
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
        except Movies.DoesNotExist as e:
            print(e)
            return HttpResponse("No data available movies")
        choices = ((movie.title, movie.title) for movie in movies)
        context = {"form": UpdateForm(choices)}
        return render(request, self.template, context)

    def post(self, request):
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
        except Movies.DoesNotExist as e:
            return redirect(request.path)
        choices = ((movie.title, movie.title) for movie in movies)
        data = UpdateForm(choices, request.POST)
        if data.is_valid():
            try:
                movie = Movies.objects.get(title=data.cleaned_data['title'])
                movie.opening_crawl = data.cleaned_data['opening_crawl']
                movie.save()
            except db.Error as e:
                print(e)
        return redirect(request.path)
