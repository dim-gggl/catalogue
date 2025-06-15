from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}".strip() or "Artiste inconnu"
        )
