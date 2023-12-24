from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


import datetime

BOOKING_TIME = ((datetime.time(9, 0, 0), '9:00am'),
                (datetime.time(11, 0, 0), '11:00am'),
                (datetime.time(13, 0, 0), '1:00pm'),
                (datetime.time(15, 0, 0), '3:00pm'),
                (datetime.time(17, 00, 0), '5:00pm'),
                (datetime.time(19, 00, 0), '7:00pm'),
                )


class Services(models.Model):

    service_name = models.CharField(max_length=250)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.service_name


class Booking(models.Model):

    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='username_booking')
    date_of_booking = models.DateField()
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE,
                                     related_name='service_name_booking')
    start_time = models.TimeField(choices=BOOKING_TIME)
    end_time = models.TimeField(editable=False, blank=True, null=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_of_booking', 'start_time']

    def __str__(self):
        return f"{self.service_name} for {self.username} on {self.date_of_booking} at {self.start_time}"

    def calculateEndTime(self):
        if self.start_time and self.service_name:
            start_datetime = datetime.datetime.combine(
                self.date_of_booking, self.start_time)
            session_length = self.service_name.session_length
            end_datetime = start_datetime + session_length
            self.end_time = end_datetime.time()
            self.save()
