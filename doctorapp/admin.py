from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DoctorModel)
admin.site.register(DepartmentModel)
admin.site.register(BookingModel)
