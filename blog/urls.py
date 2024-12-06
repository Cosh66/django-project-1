from django.urls import path
from . import views  # Import views from the current directory


urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('upload/', views.upload_image, name='upload_image'),
    path('gallery/', views.image_gallery, name='image_gallery'),
    
]