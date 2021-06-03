from django.db import models
import hashlib
import uuid


class User(models.Model):
    username = models.CharField(max_length=32, primary_key=True, null=False)
    password = models.CharField(max_length=64, null=False)
    salt = models.CharField(max_length=32, null=False)

    def __hash(self, str: str) -> str:
        return hashlib.sha256((str + self.salt).encode('utf-8')).hexdigest()

    def set_password(self, password: str):
        self.salt = uuid.uuid4().hex
        self.password = self.__hash(password)

    def check_password(self, password: str) -> bool:
        hash = self.__hash(password)
        return self.password == hash
