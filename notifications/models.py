from django.db import models

class Notification(models.Model):

    NOTIFICATION_TYPES = [
        ('General', 'General'),
        ('Queue', 'Queue'),
        ('Service', 'Service'),
        ('Emergency', 'Emergency'),
]
    

    STATUS_CHOICES = [
        ('Unread', 'Unread'),
        ('Read', 'Read'),
    ]

    title = models.CharField(max_length=100)
    message = models.TextField()
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
        default='General'
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Unread'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title