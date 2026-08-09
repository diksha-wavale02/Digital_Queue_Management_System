from django.db import models


# -------------------------
# User Model
# -------------------------
class User(models.Model):

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# -------------------------
# Profile Model
# -------------------------
class Profile(models.Model):

    phone = models.CharField(max_length=15)
    address = models.TextField()

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.full_name


# -------------------------
# Feedback Model
# -------------------------
class Feedback(models.Model):

    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.full_name


# -------------------------
# Token History Model
# -------------------------
class TokenHistory(models.Model):

    token_number = models.CharField(max_length=20)
    service_name = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Completed", "Completed"),
            ("Cancelled", "Cancelled"),
        ],
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.token_number

