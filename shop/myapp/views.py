from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from . import models
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import employee

def base(request):
    return render(request, 'base.html')

def login(request):
    if request.method == 'POST':
        eemail = request.POST.get('eemail')
        password = request.POST.get('password')
        obj_user = models.employee.objects.filter(eemail=eemail, password=password)
        if obj_user:
            return redirect('/index')
        error = 'Wrong username and password'

    return render(request, 'login.html', locals())


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        ename = request.POST['ename']
        eemail= request.POST['eemail']
        password= request.POST['password']
        new = employee(ename=ename, eemail=eemail,password=password)
        new.save()
        return redirect('/login')

    return render(request, 'registration.html')
