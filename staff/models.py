from django.db import models


class Staff(models.Model):

    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Busy", "Busy"),
        ("Offline", "Offline"),
    ]

    full_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name