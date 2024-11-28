from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include django-allauth URLs
    path('', include('blog.urls')),  # Include your app's URLs
]