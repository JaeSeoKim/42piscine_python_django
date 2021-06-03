from django.conf import settings
from django.views import View
from django.http import HttpRequest, HttpResponse
import psycopg2


class Init(View):
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT'],
    )

    def get(self, request):
        try:
            CREATE_TABEL = f"""
            CREATE TABLE ex08_planets(
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR,
                diameter INT,
                orbital_period INT,
                population BIGINT,
                rotation_period INT,
                surface_water REAL,
                terrain VARCHAR(128)
                );

            CREATE TABLE ex08_people(
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INT,
                mass REAL,
                homeworld VARCHAR(64) REFERENCES ex08_planets(name)
                );
            """

            with self.conn.cursor() as curs:
                curs.execute(CREATE_TABEL)
            self.conn.commit()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse("OK")
