from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    average_time = models.IntegerField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_name