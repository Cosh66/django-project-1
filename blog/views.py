from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import UploadedImage, Post, Comment
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
@login_required
def upload_image(request):
    if request.method == "POST":
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save(commit=False)
            uploaded_image.author = request.user
            uploaded_image.save()
            messages.success(request, f"Image uploaded successfully by {request.user.username}.")
            return redirect('image_gallery')
    else:
        form = UploadedImageForm()
    return render(request, 'blog/upload_image.html', {'form': form})


# Image gallery
def image_gallery(request):
    images = UploadedImage.objects.all().order_by('-uploaded_at')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            image_id = request.POST.get('image_id')  # Get the image ID from the hidden input field
            image = get_object_or_404(UploadedImage, id=image_id)
            comment = form.save(commit=False)
            comment.image = image
            comment.author = request.user  # Assign the logged-in user as the comment author
            comment.save()
            messages.success(request, f"Comment added successfully by {request.user.username}.")
            return redirect('image_gallery')
    else:
        form = CommentForm()
    return render(request, 'blog/image_gallery.html', {'images': images, 'form': form})


