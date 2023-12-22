from .models import Booking
from django import forms
from datetime import datetime
from django.forms.widgets import DateInput


class BookingForm(forms.ModelForm):
    """For to create and edit a Race Day booking"""
    class Meta:
        model = Booking
        fields = ["date_of_booking", "service_name", "start_time"]
        widgets = {'date_of_booking': DateInput(attrs={'type': 'date'}), }

        labels = {
            'date_of_booking': 'Date',
            'service_name': 'Race',
            'start_time': 'Time',
        }
