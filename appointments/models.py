from django.db import models
from services.models import Service
from locations.models import Location


class Appointment(models.Model):

    customer_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=15)

    category = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='appointments',
        blank=True,
        null=True,
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        default='Booked'
    )

    def __str__(self):
        return self.customer_name