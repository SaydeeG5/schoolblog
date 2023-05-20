from django.views.generic import TemplateView
from django.views.generic.edit import CreateView 
#from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render 
from django.urls import reverse_lazy 

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")



