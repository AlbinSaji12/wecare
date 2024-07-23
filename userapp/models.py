from django.db import models


# Create your models here.
class UserModel(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    disease = models.CharField(max_length=40)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        db_table = "user"
