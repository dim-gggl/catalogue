from django.db import models
from django.conf import settings
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



TECHNIQUES = [
    "Peinture à l'huile",
    "Aquarelle",
    "Photographie argentique",
    "Art numérique",
    "Fusain",
    "Crayon",
    "Impression 3D",
    "Acrylique",
    "Gouache",
    "Pastel",
    "Tempera",
    "Encaustique",
    "Encre",
    "Fresque",
    "Collage",
    "Assemblage",
    "Chiaroscuro",
    "Divisionnisme",
    "Cire perdue",
    "Trompe-l'œil",
    "Impasto",
    "Sgraffito",
    "Glazing",
    "Hatching",
    "Stippling",
    "Blending",
    "Scumbling",
    "Dry brushing",
    "Wash",
    "Underpainting",
    "Alla prima",
    "Plein air",
    "Mixed media",
    "Spray painting",
    "Airbrushing",
    "Screen printing",
    "Lithographie",
    "Eau-forte",
    "Woodcut",
    "Linocut"
]

SUPPORTS = [
    "Toile",
    "Papier glacé",
    "Marbre",
    "Papier",
    "Panneau de bois",
    "Masonite",
    "Métal",
    "Ivoire",
    "Vélin",
    "Soie",
    "Clayboard",
    "Verre",
    "Plâtre",
    "Cuir",
    "Tissu",
    "Carton",
    "MDF",
    "Panneau durci",
    "Plexiglas",
    "Tuiles céramiques",
    "Pierre"
]

ART_TYPES = [
    "Peinture",
    "Photographie",
    "Dessin",
    "Sculpture",
    "Gravure",
    "Art d'installation",
    "Art de performance",
    "Art numérique",
    "Art vidéo",
    "Céramique",
    "Textiles",
    "Art du verre",
    "Métallerie",
    "Joaillerie",
    "Architecture",
    "Design graphique",
    "Illustration",
    "Calligraphie",
    "Bande dessinée",
    "Art de la bande dessinée"
]



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
        name="Signé", default=False,
        choices=[("True", "Oui"), ("False", "Non")]
    )
    contextual_references = models.ManyToManyField(
        ContextualReference, blank=True, related_name="artworks"
    )
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name=_("artworks")
    )

    @property
    def is_in_wishlist(self):
        user = self.request.user
        return self in user.wishlist

    def __str__(self):
        return self.title or f"Œuvre sans titre #{self.id}"

    class Meta:
        ordering = ["-acquisition_date", "title"]
