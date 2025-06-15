from django.db import models


class Exhibition(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_planned = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
