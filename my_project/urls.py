from django.contrib import admin
from django.urls import path, include  # Import both 'path' and 'include'
from django.contrib.auth.views import LogoutView  # Import LogoutView for logout functionality

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout functionality
    path('', include('blog.urls')),  # Include URLs from the blog app
]