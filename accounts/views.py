from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import User

class UserCreateView(CreateView):
    model = User
    template_name =  'accounts/login.html'
    fields = ('name', 'password')

