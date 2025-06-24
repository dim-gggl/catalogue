from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    pseudonym = models.CharField(max_length=100, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    biography = models.TextField(blank=True)

    @property
    def pseudonym(self):
        return self.pseudonym

    @pseudonym.setter
    def pseudonym(self, value):
        if value:
            self.pseudonym = value
        if not self.pseudonym and not value:
            if any(self.first_name, self.last_name):
                self.pseudonym = self.first_name + " " + self.last_name
            else:
                self.pseudonym = "Unknown"
            
    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}".strip() or "Unknown artist"
        )
