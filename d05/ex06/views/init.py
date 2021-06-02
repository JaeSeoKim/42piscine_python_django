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
                release_date DATE NOT NULL,
                created TIMESTAMP NOT NULL DEFAULT NOW(),
                updated TIMESTAMP NOT NULL DEFAULT NOW()
                );

            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON {self.TABLE_NAME} FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
            """

            with self.conn.cursor() as curs:
                curs.execute(CREATE_TABEL)
            self.conn.commit()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse("OK")
