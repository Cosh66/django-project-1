from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),  # Include the 'blog' app URLs here
    path("accounts/", include("allauth.urls")),
]