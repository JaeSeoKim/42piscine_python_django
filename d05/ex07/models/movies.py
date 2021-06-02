from django.db import models
from django.utils.timezone import now


class Movies(models.Model):
    class Meta:
        db_table = 'ex07_movies'

    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    created = models.DateTimeField(
        auto_now_add=True, null=False)
    updated = models.DateTimeField(
        auto_now=True, null=False)

    def __str__(self) -> str:
        return self.title
