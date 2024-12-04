from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.shortcuts import redirect


STATUS = ((0, "Draft"), (1, "Published"))


# Image Upload Model
class UploadedImage(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')  # Ensure CloudinaryField is used here
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title
def image_gallery(request):
    images = UploadedImage.objects.all().order_by('-uploaded_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Create the comment object but don't save it yet
            comment.author = request.user  # Set the author as the currently logged-in user
            comment.image = UploadedImage.objects.get(id=request.POST.get('image_id'))  # Associate the image
            comment.save()  # Save the comment to the database
            return redirect('image_gallery')

    else:
        form = CommentForm()

    return render(request, 'blog/image_gallery.html', {'images': images, 'form': form})



# Blog Post Model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Title of the post
    slug = models.SlugField(max_length=200, unique=True)  # Slug for the URL
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"  # Link to user
    )
    featured_image = CloudinaryField('image', default='placeholder')  # Cloudinary image
    content = models.TextField()  # Post content
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_on = models.DateTimeField(auto_now=True)  # Timestamp for updates
    status = models.IntegerField(choices=STATUS, default=0)  # Draft or Published
    excerpt = models.TextField(blank=True)  # Short preview text

    class Meta:
        ordering = ["-created_on"]  # Order by most recent posts

    def __str__(self):
        return f"{self.title} | written by {self.author}"


# Comment Model
class Comment(models.Model):
    image = models.ForeignKey(UploadedImage, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"  # Link to user
    )
    body = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    approved = models.BooleanField(default=False)  # Moderation status

    class Meta:
        ordering = ["-created_at"]  # Order by most recent comments

    def __str__(self):
        return f"{self.body[:20]}... by {self.author}"  # Truncated display in admin


    
   