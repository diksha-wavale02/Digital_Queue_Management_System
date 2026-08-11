from django.db import models

class Staff(models.Model):
    full_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=10, default='Active')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'staff_staff'
        managed = False

    def __str__(self): 
        return self.full_name


# NAYA MODEL YE ADD KARO
class Token(models.Model):
    token_number = models.CharField(max_length=10, unique=True)
    service = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'queue_token'
        ordering = ['-created_at']

    def __str__(self):
        return f"Token {self.token_number}"
        return self.full_name

    