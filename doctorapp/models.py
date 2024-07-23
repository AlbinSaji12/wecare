from django.db import models
from userapp.models import UserModel

# Create your models here.
class DepartmentModel(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=30)
    department_image = models.ImageField(upload_to='image')
    
    class Meta:
        db_table = "doctordepartment"
        

class DoctorModel(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    doctor_name = models.CharField(max_length=30)
    doctor_specialization = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    doctor_phone = models.CharField(max_length=30)
    doctor_email = models.EmailField()
    doctor_image = models.ImageField(upload_to='image')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    password = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=30)
    

    class Meta:
        db_table = "doctor"



class BookingModel(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    Patient_name = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    Appointment_date = models.DateField()
    Appointment_time = models.TimeField()
    
    status = models.CharField(max_length=30)

    class Meta:
      db_table = "booking"






