from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage
    path('about/', views.about, name='about'),
    path('upload/', views.upload_image, name='upload_image'),
    path('gallery/', views.image_gallery, name='image_gallery'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('home/', views.index, name='home'),  # Add this for 'home'
]

