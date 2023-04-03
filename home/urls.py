from django.contrib import admin
from django.urls import path, include

from home.views import home

app_name='home'

urlpatterns = [
    path('home/', home, name='home'),
]
