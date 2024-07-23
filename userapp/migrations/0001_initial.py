# Generated by Django 5.0.3 on 2024-07-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('disease', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_no', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]