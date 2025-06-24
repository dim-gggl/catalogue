from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .artwork import Artwork

class Wishlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wishlist"
    )
    added_at = models.DateTimeField(auto_now_add=True)
    artworks = models.ManyToManyField(
        Artwork,
        related_name=_("wishlist")
    )

    class Meta:
        unique_together = ("user", "artworks")

    def add_artwork(self, artwork):
        self.artworks.add(artwork)
        self.save()
    
    def remove_artwork(self, artwork):
        self.artworks.remove(artwork)
        self.save()

    def is_in_wishlist(self, artwork):
        return artwork in self.artworks.all()

    def __str__(self):
        return f"{self.user.username} - {self.artworks}"
