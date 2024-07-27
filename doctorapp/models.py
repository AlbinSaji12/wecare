from django.db import models
from userapp.models import UserModel

# Create your models here.
class DepartmentModel(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=30)
    department_image = models.ImageField(upload_to='image')
    
    class Meta:
        db_table = "doctordepartment"
    def __str__(self):
        return self.department_name



class DoctorModel(models.Model):
    DAYS_OF_WEEK = [
        ('MO', 'Monday'),
        ('TU', 'Tuesday'),
        ('WE', 'Wednesday'),
        ('TH', 'Thursday'),
        ('FR', 'Friday'),
        ('SA', 'Saturday'),
        ('SU', 'Sunday'),
    ]

    doctor_id = models.IntegerField(primary_key=True)
    doctor_name = models.CharField(max_length=30)
    doctor_specialization = models.ForeignKey('DepartmentModel', on_delete=models.CASCADE)
    doctor_phone = models.CharField(max_length=30)
    doctor_email = models.EmailField()
    doctor_image = models.ImageField(upload_to='image')
    start_date = models.CharField(max_length=2, choices=DAYS_OF_WEEK, null=True)
    end_date = models.CharField(max_length=2, choices=DAYS_OF_WEEK, null=True)
    time = models.TimeField(null=True)
    password = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "doctor"
    def __str__(self):
        return self.doctor_name
     



class BookingModel(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    Patient_name = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    Appointment_date = models.DateField()
    Appointment_time = models.TimeField()
    
    status = models.CharField(max_length=30)

    class Meta:
      db_table = "booking"






