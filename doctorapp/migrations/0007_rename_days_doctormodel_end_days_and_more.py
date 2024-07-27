# Generated by Django 5.0.3 on 2024-07-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0006_remove_doctormodel_date_doctormodel_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctormodel',
            old_name='days',
            new_name='end_days',
        ),
        migrations.AddField(
            model_name='doctormodel',
            name='start_days',
            field=models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=2, null=True),
        ),
    ]
