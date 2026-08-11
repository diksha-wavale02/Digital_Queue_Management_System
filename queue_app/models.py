from django.db import models
from appointments.models import Appointment


class Queue(models.Model):

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE
        
    )

    token_number = models.IntegerField()

    status = models.CharField(
        max_length=20,
        default='Waiting'
    )

    def __str__(self):

        return f"Q{self.token_number:03d}"