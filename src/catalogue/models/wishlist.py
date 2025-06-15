from django.db import models
from django.conf import settings

from .artwork import Artwork

class Wishlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wishlist"
    )
    artwork = models.ForeignKey(
        Artwork, on_delete=models.CASCADE,
        related_name="wishlisted_by"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "artwork")

    def __str__(self):
        return f"{self.user.username} - {self.artwork}"
