from django.db import models

class Report(models.Model):
    REPORT_TYPES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ]

    report_name = models.CharField(max_length=100)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    total_tokens = models.PositiveIntegerField(default=0)
    completed_tokens = models.PositiveIntegerField(default=0)
    cancelled_tokens = models.PositiveIntegerField(default=0)
    average_wait_time = models.PositiveIntegerField(help_text="Minutes", default=0)
    generated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_name} ({self.report_type})"