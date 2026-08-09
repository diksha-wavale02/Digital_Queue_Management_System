from django import forms
from .models import Staff


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            "full_name",
            "employee_id",
            "department",
            "service",
            "phone",
            "email",
            "status",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter full name",
            }),
            "employee_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter employee ID",
            }),
            "department": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter department",
            }),
            "service": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter service",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email",
            }),
            "status": forms.Select(attrs={
                "class": "form-control",
            }),
        }