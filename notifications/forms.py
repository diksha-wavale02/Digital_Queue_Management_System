from django import forms
from .models import Notification


class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification

        fields = [
            'title',
            'message',
            'notification_type',
            'status',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Notification Title'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter Notification Message'
            }),

            'notification_type': forms.Select(attrs={
                'class': 'form-control'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),

        }