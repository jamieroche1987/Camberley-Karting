# Generated by Django 4.2.8 on 2023-12-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karting', '0004_booking_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
