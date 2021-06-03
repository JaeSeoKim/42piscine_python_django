from django.conf import settings
from django.db import models


class TipModel(models.Model):
    content = models.TextField(null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
