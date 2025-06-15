from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
