from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post, UploadedImage
from .forms import UploadedImageForm

# Home page and list of posts
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)  # Only show published posts
    template_name = "blog/index.html"
    paginate_by = 6


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
            return redirect('image_gallery')  # Redirect to gallery
    else:
        form = UploadedImageForm()
    return render(request, 'blog/upload_image.html', {'form': form})


# Image gallery
def image_gallery(request):
    images = UploadedImage.objects.all().order_by('-uploaded_at')
    return render(request, 'blog/image_gallery.html', {'images': images})

