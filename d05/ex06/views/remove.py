from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from ..forms import RemoveForm
import psycopg2


class Remove(View):
    TABLE_NAME = "ex06_movies"
    template = "ex06/remove.html"
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT'],
    )

    def get(self, request):
        SELECT_TABEL = f"""
            SELECT * FROM {self.TABLE_NAME};
            """
        try:
            with self.conn.cursor() as curs:
                curs.execute(SELECT_TABEL)
                movies = curs.fetchall()
            context = {'form': RemoveForm(choices=(
                (movie[0], movie[0]) for movie in movies))}
            return render(request, self.template, context)
        except Exception as e:
            print(e)
            return HttpResponse("No data available")

    def post(self, request):
        SELECT_TABEL = f"""
            SELECT title FROM {self.TABLE_NAME};
            """
        try:
            with self.conn.cursor() as curs:
                curs.execute(SELECT_TABEL)
                movies = curs.fetchall()
            choices = (
                (movie[0], movie[0]) for movie in movies)
        except Exception as e:
            print(e)
        data = RemoveForm(choices, request.POST)
        DELETE_SQL = f"""
            DELETE FROM {self.TABLE_NAME} WHERE title = %s
            """
        if data.is_valid() == True:
            try:
                with self.conn.cursor() as curs:
                    curs.execute(DELETE_SQL, [data.cleaned_data['title']])
                self.conn.commit()
            except Exception as e:
                print(e)
        return redirect(request.path)
