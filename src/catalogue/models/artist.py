from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    pseudonym = models.CharField(max_length=100, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    biography = models.TextField(blank=True)
    
    # @property
    # def pseudonym(self):
        

    # @pseudonym.setter
    # def pseudonym(self, value):
    #     if value:
    #         self.pseudonym = value
    #     else:
    #         self.pseudonym = f"{self.first_name} {self.last_name}"
    
    def display_name(self):
        """Return a user friendly name for the artist."""
        if self.pseudonym:
            return self.pseudonym
        name = f"{self.first_name} {self.last_name}".strip()
        return name or "Unknown artist"

    def __str__(self):
        return self.display_name