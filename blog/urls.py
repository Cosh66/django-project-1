from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('upload/', views.upload_image, name='upload_image'),  # Upload page
    path('gallery/', views.image_gallery, name='image_gallery'),  # Image gallery
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # Post detail
    # Removed 'signup/' because Allauth handles it
]


