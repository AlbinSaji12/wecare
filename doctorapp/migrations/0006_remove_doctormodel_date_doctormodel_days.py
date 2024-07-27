# Generated by Django 5.0.3 on 2024-07-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0005_rename_booking_date_doctormodel_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctormodel',
            name='date',
        ),
        migrations.AddField(
            model_name='doctormodel',
            name='days',
            field=models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=2, null=True),
        ),
    ]
