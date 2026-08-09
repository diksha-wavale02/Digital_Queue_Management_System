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
        db_table = 'staff_staff'  # existing table
        managed = False  # django migration nahi chalega

    def __str__(self):
        return self.full_name