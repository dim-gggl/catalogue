from django.db import models


class ContextualReference(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    reference_type = models.CharField(
        max_length=100,
        choices=[
            ("EXHIBITION_CATALOGUE", "Catalogue d'exposition"),
            ("ALBUM", "Album BD"),
            ("BOOK", "Ouvrage critique"),
            ("MAGAZINE", "Magazine"),
            ("OTHER", "Autre")
        ],
        default="OTHER"
    )
    author = models.CharField(max_length=255, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    isbn = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
