from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(("Article title"), max_length=64, null=False)
    author: User = models.ForeignKey(User, verbose_name=(
        "Article author"), on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(
        ("Article Created"), auto_now=False, auto_now_add=True)
    synopsis = models.CharField(
        ("aricle synopsis"), max_length=312, null=False)
    content = models.TextField(("article content"))

    def __str__(self) -> str:
        return str(self.title)


class UserFavouriteArticle(models.Model):
    user: User = models.ForeignKey(User, verbose_name=(
        "UserFavouriteArticle user"), on_delete=models.CASCADE, null=False)
    article: Article = models.ForeignKey(Article, verbose_name=(
        "UserFavouriteArticle article"), on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return str(self.article.title)
