from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import psycopg2


class Display(View):
    template = 'ex06/display.html'
    TABLE_NAME = "ex06_movies"
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
            return render(request, self.template, {"movies": movies})
        except Exception as e:
            return HttpResponse("No data available")
