# forms.py
from django import forms
from .models import UploadImage

class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserImage(forms.ModelForm):
    class Meta:
        # To specify the model to be used to create form
        model = UploadImage
        # It includes all the fields of model
        fields = '__all__'