from django import forms
from .models import User, Feedback


# -------------------------
# Profile Form
# -------------------------
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["full_name", "email", "phone"]

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter full name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter email"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter phone number"
                }
            ),
        }


# -------------------------
# Feedback Form
# -------------------------
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ["message"]

        widgets = {
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your feedback",
                    "rows": 5
                }
            ),
        }

