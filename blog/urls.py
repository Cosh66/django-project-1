from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='account_login'),  # Login page
]