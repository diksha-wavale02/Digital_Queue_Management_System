from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment

        fields = [
            'customer_name',
            'phone_number',
            'category',
            'service',
            'location',
            'appointment_date',
            'appointment_time'
        ]

        widgets = {

            'customer_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter customer name'
                }
            ),

            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter phone number'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),

            'service': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'location': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'appointment_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'appointment_time': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                }
            ),
        }