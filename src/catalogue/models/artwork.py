from django.db import models
from django.utils.translation import gettext_lazy as _

from .art import Art
from .support import Support
from .technique import Technique
from .artist import Artist
from .collection import Collection
from .tag import Tag
from .exhibition import Exhibition
from .location import Location
from .contextual_reference import ContextualReference

from ..art_constants import (ART_TYPES, TECHNIQUES, SUPPORTS)

class Artwork(models.Model):
    title = models.CharField(max_length=200, blank=True)
    artist = models.ForeignKey(
        Artist, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="artworks"
    )
    art_type = models.ForeignKey(
        Art, null=True, blank=True,
        on_delete=models.SET_NULL
    )
    support = models.ForeignKey(
        Support, null=True, blank=True,
        on_delete=models.SET_NULL
    )
    technique = models.ForeignKey(
        Technique, null=True, blank=True, on_delete=models.SET_NULL
    )

    creation_year = models.IntegerField(null=True, blank=True)
    width_cm = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    height_cm = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    depth_cm = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    weight_kg = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )

    acquisition_date = models.DateField(null=True, blank=True)
    acquisition_place = models.CharField(max_length=255, blank=True)
    price_eur = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    provenance = models.TextField(blank=True)

    notes = models.TextField(blank=True)
    is_framed = models.BooleanField(default=False)
    is_on_loan = models.BooleanField(default=False)

    collections = models.ManyToManyField(
        Collection, blank=True, related_name="artworks"
    )
    tags = models.ManyToManyField(
        Tag, blank=True, related_name="artworks"
    )
    exhibitions = models.ManyToManyField(
        Exhibition, blank=True, related_name="artworks"
    )
    location = models.ForeignKey(
        Location, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="artworks"
    )
    is_signated = models.BooleanField(
        name="is_signed", default=False,
        choices=[("True", "Yes"), ("False", "No")]
    )
    contextual_references = models.ManyToManyField(
        ContextualReference, blank=True, related_name="artworks"
    )

    def is_in_wishlist(self, user):
        return self in user.wishlist

    def __str__(self):
        return self.title or f"{'Untitled'} #{self.id}"

    class Meta:
        ordering = ["-acquisition_date", "title"]
