from django.conf import settings
from django.views import View
from django.http import HttpRequest, HttpResponse
import psycopg2


class Init(View):
    TABLE_NAME = "ex06_movies"
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
            CREATE TABLE {self.TABLE_NAME}(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
                );
            """
            with self.conn.cursor() as curs:
                curs.execute(CREATE_TABEL)
            self.conn.commit()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse("OK")
