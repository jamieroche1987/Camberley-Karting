from .models import Booking, Services, BOOKING_TIME
from django import forms
from datetime import datetime
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):

    """
    Form to create and edit a Race Day booking.
    Fields:
        - date_of_booking: Date field for selecting the booking date.
        - service_name: Dropdown for selecting the haircut service.
        - start_time: Time field for selecting the booking time.
    Widget:
        - date_of_booking: DateInput widget with type 'date' for a date picker.
    Labels:
        - date_of_booking: 'Date'
        - service_name: 'Race'
        - start_time: 'Time'
    """
    class Meta:
        model = Booking
        fields = ["date_of_booking", "service_name", "start_time"]
        widgets = {'date_of_booking': DateInput(attrs={'type': 'date'}), }

        labels = {
            'date_of_booking': 'Date',
            'service_name': 'Race',
            'start_time': 'Time',
        }

    # class Selectpackage(forms.ModelForm):
    #     class Meta:
    #         model = Booking
    #         fields = ["date_of_booking", "service_name",]
    #         widgets = {'date_of_booking': DateInput(attrs={'type': 'date'}),
    #                    'service_name': forms.HiddenInput(), }

    #         labels = {
    #             'date_of_booking': 'Date',
    #             'service_name': 'Haircut',
    #             }

    # Form Wizard Forms


class SelectPackageForm(forms.ModelForm):
        class Meta:
        model = Services
        fields = ('service_name',)
        # widgets = {'service_name': forms.Select(attrs={'class': 'service-buttons'})}  # to use buttons for the options

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        return context


class SelectDateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date_of_booking',)
        widgets = {'date_of_booking': DateInput(attrs={'type': 'date'})}


class SelectTimeForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('start_time',)
