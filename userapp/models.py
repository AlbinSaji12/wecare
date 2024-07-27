from django.db import models


# Create your models here.
class UserModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
     
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    disease = models.CharField(max_length=40)
    age = models.IntegerField()
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES,null=True)
    phone_no = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        db_table = "user"
    def __str__(self):
        return self.user_name   
