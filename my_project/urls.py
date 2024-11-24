from django.contrib import admin
from django.urls import path, include  # Import include to use app's urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),  # Summernote URL
    path('', include('blog.urls')),  # Root URL points to blog.urls (update 'blog' with your app name)
]