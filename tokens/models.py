from django.db import models


class Token(models.Model):
    token_number = models.IntegerField()
    service = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Waiting', 'Waiting'),
            ('In Process', 'In Process'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Waiting'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Token {self.token_number}"