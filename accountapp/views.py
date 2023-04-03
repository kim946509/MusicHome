from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView


# Create your views here.
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
