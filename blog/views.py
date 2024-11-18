from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Post

# Home page: List of blog posts
class PostList(ListView):
    model = Post
    template_name = 'post_list.html'  # Points to the template for the home page
    context_object_name = 'posts'    # Name used in the template to loop through posts

# Post detail page: Single blog post
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})


