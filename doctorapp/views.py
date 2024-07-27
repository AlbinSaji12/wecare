from django.shortcuts import render
from django.http import HttpResponse
from doctorapp.models import *

# Create your views here.
def login(request):
    return render(request, "login.html")

