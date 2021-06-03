from django.conf import settings
from django.http.response import HttpResponse
from django.views import View
import psycopg2


def parsing_planet(line: str):
    line = line.split('	')
    planet = {
        'name': line[0].strip() if line[0].strip() != 'NULL' else None,
        'climate': line[1].strip() if line[1].strip() != 'NULL' else None,
        'diameter': line[2].strip() if line[2].strip() != 'NULL' else None,
        'orbital_period': line[3].strip() if line[3].strip() != 'NULL' else None,
        'population': line[4].strip() if line[4].strip() != 'NULL' else None,
        'rotation_period': line[5].strip() if line[5].strip() != 'NULL' else None,
        'surface_water': line[6].strip() if line[6].strip() != 'NULL' else None,
        'terrain': line[7].strip() if line[7].strip() != 'NULL' else None,
    }
    return planet


def parsing_people(line: str):
    line = line.split('	')
    people = {
        'name': line[0].strip() if line[0].strip() != 'NULL' else None,
        'birth_year': line[1].strip() if line[1].strip() != 'NULL' else None,
        'gender': line[2].strip() if line[2].strip() != 'NULL' else None,
        'eye_color': line[3].strip() if line[3].strip() != 'NULL' else None,
        'hair_color': line[4].strip() if line[4].strip() != 'NULL' else None,
        'height': line[5].strip() if line[5].strip() != 'NULL' else None,
        'mass': line[6].strip() if line[6].strip() != 'NULL' else None,
        'homeworld': line[7].strip() if line[7].strip() != 'NULL' else None,
    }
    return people


class Populate(View):
    table_planets = "ex08_planets"
    table_people = "ex08_people"
    planets = []
    people = []
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT'],
    )

    def get(self, request):
        try:
            with open('data/planets.csv') as f:
                self.planets = [parsing_planet(line) for line in f.readlines()]
            with open('data/people.csv') as f:
                self.people = [parsing_people(line) for line in f.readlines()]
        except Exception as e:
            return HttpResponse(e)

        INSERT_PLANET = f"""
            INSERT INTO {self.table_planets}
            (
                name,
                climate,
                diameter,
                orbital_period,
                population,
                rotation_period,
                surface_water,
                terrain
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
            """
        INSERT_PEOPLE = f"""
            INSERT INTO {self.table_people}
            (
                name,
                birth_year,
                gender,
                eye_color,
                hair_color,
                height,
                mass,
                homeworld
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
            """

        result = []
        curs = self.conn.cursor()
        for planet in self.planets:
            try:
                curs.execute(INSERT_PLANET, [
                    planet['name'],
                    planet['climate'],
                    planet['diameter'],
                    planet['orbital_period'],
                    planet['population'],
                    planet['rotation_period'],
                    planet['surface_water'],
                    planet['terrain'],
                ])
                result.append("OK")
                self.conn.commit()
            except psycopg2.DatabaseError as e:
                self.conn.rollback()
                result.append(e)
        for people in self.people:
            try:
                curs.execute(INSERT_PEOPLE, [
                    people['name'],
                    people['birth_year'],
                    people['gender'],
                    people['eye_color'],
                    people['hair_color'],
                    people['height'],
                    people['mass'],
                    people['homeworld'],
                ])
                result.append("OK")
                self.conn.commit()
            except psycopg2.DatabaseError as e:
                self.conn.rollback()
                result.append(e)
        curs.close()
        return HttpResponse("<br/>".join(str(i) for i in result))
