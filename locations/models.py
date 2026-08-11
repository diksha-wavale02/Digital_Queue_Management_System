from django.db import models
from services.models import Service


class Location(models.Model):

    category = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="locations"
    )

    name = models.CharField(
        max_length=150
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    latitude = models.FloatField(
        blank=True,
        null=True
    )

    longitude = models.FloatField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} - {self.city}"