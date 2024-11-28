from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Homepage
    path('about/', views.about, name='about'),  # About Page
    path('upload/', views.upload, name='upload'), # Upload Page
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Post Detail
]

