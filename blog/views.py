from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post, UploadedImage, Comment
from .forms import UploadedImageForm, CommentForm


# Home page and list of posts
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)  # Only show published posts
    template_name = "blog/index.html"
    paginate_by = 6  # Adjust pagination as needed


# Single post detail
def post_detail(request, slug):
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})


# About page
def about(request):
    return render(request, "blog/about.html")


# Upload images
def upload_image(request):
    if request.method == "POST":
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_gallery')  # Redirect to the gallery after upload
    else:
        form = UploadedImageForm()
    return render(request, 'blog/upload_image.html', {'form': form})


# Image gallery
def image_gallery(request):
    images = UploadedImage.objects.all().order_by('-uploaded_at')  # Fetch all images

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            image_id = request.POST.get('image_id')  # Get the image ID from the hidden input field
            image = get_object_or_404(UploadedImage, id=image_id)
            comment = form.save(commit=False)
            comment.image = image
            comment.author = request.user  # Set the author to the logged-in user
            comment.save()
            return redirect('image_gallery')  # Reload the page after comment submission
    else:
        form = CommentForm()

    return render(request, 'blog/image_gallery.html', {'images': images, 'form': form})


# Upload page (optional, if needed separately)
def upload_page(request):
    return render(request, 'upload.html')


# User signup
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('image_gallery')  # Redirect to the gallery
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form}) 

