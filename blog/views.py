from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post, UploadedImage
from .forms import UploadedImageForm  # Ensure this is added if you created forms.py

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
    return render(request, 'blog/index.html') 


# Function-based view for the about page
def about(request):
    return render(request, 'blog/about.html')


# Function-based view for uploading images
def upload_image(request):
    """
    Handles image uploads. Displays a form for uploading and saves valid images.
    """
    if request.method == "POST":
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the uploaded image
            return redirect('image_gallery')  # Redirect to gallery view after upload
    else:
        form = UploadedImageForm()
    return render(request, 'blog/upload_image.html', {'form': form})


# Function-based view for the image gallery
def image_gallery(request):
    """
    Displays a gallery of uploaded images.
    """
    images = UploadedImage.objects.all().order_by('-uploaded_at')  # Fetch images
    return render(request, 'blog/image_gallery.html', {'images': images})


# Function-based view for the upload page (already included)
def upload(request):
    return render(request, 'blog/upload.html')


# Function-based view for the index page (already included)
def index(request):
    return render(request, 'blog/index.html')  

