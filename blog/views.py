from django.shortcuts import render
from django.views import generic
from .models import Post


# Class-based view for the list of posts
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)  # Only show posts with status=1
    template_name = "blog/index.html"  # Template to render the list of posts
    paginate_by = 6  # Pagination: 6 posts per page


# Function-based view for a single post detail
def post_detail(request, slug):
    """
    Displays an individual blog post.
    Retrieves the post based on its slug and status.
    """
    queryset = Post.objects.filter(status=1)  # Filter published posts
    post = get_object_or_404(queryset, slug=slug)  # Get post by slug
    return render(request, "blog/post_detail.html", {"post": post})


# Function-based view for the homepage
def home(request):
    return render(request, 'home.html')  # Correct path for index.html


# Function-based view for the about page
def about(request):
    """
    Renders the about page.
    """
    return render(request, "blog/about.html")

def upload(request):
    return render(request, 'blog/upload.html')

