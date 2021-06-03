from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import psycopg2
import json


class Display(View):
    template = 'ex08/display.html'
    table_planets = "ex08_planets"
    table_people = "ex08_people"
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT'],
    )

    def get(self, request):
        SELECT_TABEL = f"""
            SELECT
                {self.table_people}.name,
                {self.table_people}.homeworld,
                {self.table_planets}.climate
            FROM {self.table_planets}, {self.table_people}
            where
                {self.table_planets}.climate
                like '%windy%'
            order by {self.table_planets}.name;
            """
        try:
            with self.conn.cursor() as curs:
                curs.execute(SELECT_TABEL)
                datas = curs.fetchall()
            return render(request, self.template, {'datas': datas})
        except Exception as e:
            return HttpResponse("No data available")
