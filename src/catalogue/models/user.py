from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from ..managers import UserManager
from .wishlist import Wishlist

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, max_length=800)
    profile_picture = models.ImageField(
        upload_to=_('profile_pictures/'),
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __repr__(self):
        return f"<User: id={self.pk}>"

    def __str__(self):
        return f"User: {self.username}"
