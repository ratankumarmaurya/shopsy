from django.db import models
from django.forms import ModelForm

# Create your models here.
class employee(models.Model):
    ename = models.CharField(max_length=50, unique=True)
    eemail=models.TextField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "employee"


class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.caption
