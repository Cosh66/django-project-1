from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
]

from django.shortcuts import render

def home(request):
    return render(request, 'blog/index.html')

