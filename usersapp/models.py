from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4,
                            verbose_name='uuid')
    username = models.CharField(max_length=64, unique=True,
                                verbose_name='username')
    password = models.CharField(max_length=128, verbose_name='password')
    first_name = models.CharField(max_length=64, verbose_name='first name')
    last_name = models.CharField(max_length=64, verbose_name='last name')
    email = models.EmailField(unique=True, verbose_name='e-mail')

    def __str__(self):
        return self.username
