from django.db import models


class ServiceCategory(models.Model):

    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Service(models.Model):

    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="services",
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=100
    )

    duration = models.IntegerField(
        default=15
    )

    def __str__(self):
        return self.name