# Generated by Django 4.2.8 on 2023-12-27 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karting', '0003_remove_services_description_services_session_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='message',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
