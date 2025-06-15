from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True, blank=True
    )

    def __str__(self):
        return self.username
