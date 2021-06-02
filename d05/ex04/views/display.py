from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import psycopg2


TABLE_NAME = "ex04_movies"


class Display(View):
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT'],
    )

    def get(self, request):
        SELECT_TABEL = """
            SELECT * FROM {table_name};
            """.format(table_name=TABLE_NAME)
        try:
            with self.conn.cursor() as curs:
                curs.execute(SELECT_TABEL)
                movies = curs.fetchall()
            return render(request, 'ex02/display.html', {"movies": movies})
        except Exception as e:
            return HttpResponse("No data available")
