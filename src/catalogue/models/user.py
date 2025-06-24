from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from ..managers import UserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, max_length=800)
    profile_picture = models.ImageField(
        upload_to=_('profile_pictures/'),
        null=True,
        blank=True
    )
    wishlist = models.JSONField(
        default=list, blank=True, null=True,
        help_text=_("List of artwork references in the wishlist")
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __repr__(self):
        return _(f"<User: id={self.pk}>")

    def __str__(self):
        return _(f"User: {self.username}")
