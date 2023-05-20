# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import CustomUser
from django import forms 




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta(UserCreationForm): 
        model = User
        fields = ["username","email","password1","password2"]