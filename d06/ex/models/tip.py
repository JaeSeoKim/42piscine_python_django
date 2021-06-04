from django.contrib.auth.models import User
from django.db import models


class TipModel(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)


class VoteModel(models.Model):
    id = models.AutoField(primary_key=True)
    vote = models.ForeignKey(TipModel, on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    type = models.BooleanField(null=False, default=True)
