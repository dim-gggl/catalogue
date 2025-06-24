from django.db import models

from ..const import CONTEXTUAL_SUPPORTS as CHOICES


class ContextualReference(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    reference_type = models.CharField(
        max_length=100,
        choices=[
            (choice, choice.lower().replace("_", " ").title()) for choice in CHOICES
        ],
        default="OTHER"
    )
    author = models.CharField(max_length=255, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    isbn = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
