from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.http import HttpRequest
from . import models
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import employee
from .models import UploadImage
from .forms import UserImage



def base(request):
    return render(request, 'base.html')

def product(request):
    return render(request, 'product.html')


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
    form2 = UserImage()
    img = UploadImage.objects.all()
    return render(request, 'index.html', {'img': img, 'form': form2})
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


class UserImageForm:
    pass


def photo (request):
    if request.method == "POST":
        form = UserImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form =UserImage()
    img = UploadImage.objects.all()
    return render(request, 'photo.html', {'img': img, 'form': form})
    # if request.method == 'POST':
    #     form = UserImage(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #           # Getting the current instance object to display in the template
    #         # Getting the current instance object to display in the template
    #         img_object = form.instance
    #
    #         return render(request, 'photo.html', {'form': form, 'img_obj': img_object})
    # else:
    #     form = UserImage()
    #
    # return render(request, 'photo.html', {'form': form})

    # return render(request,'photo.html')

def showphoto(request):
    form2 = UserImage()
    img = UploadImage.objects.all()
    return render(request, 'showphoto.html', {'img': img, 'form': form2})
    # your_instance = UploadImage.objects.all()  # Replace with your own logic to retrieve the instance
    # return render(request, 'showphoto.html', {'your_instance': your_instance})
    # return render(request,'showphoto.html')


def detail(request):
    return render(request,'product_detail.html')
