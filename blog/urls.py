from django.urls import path
from .views import PostList, post_detail

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),  # Home page: List of posts
    path('post/<slug:slug>/', post_detail, name='post_detail'),  # Post detail page
]


