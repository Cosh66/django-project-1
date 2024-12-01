from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

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
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"  # Link to post
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"  # Link to user
    )
    body = models.TextField()  # Comment content
    approved = models.BooleanField(default=False)  # Moderation status
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

    def __str__(self):
        return f"{self.body[:20]}... by {self.author}"  # Truncated display in admin


# Image Upload Model (Consolidated and Updated)
class UploadedImage(models.Model):
    title = models.CharField(max_length=255)  # Title field for the image
    image = CloudinaryField('image')  # CloudinaryField for storing images
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the upload

    class Meta:
        ordering = ["-uploaded_at"]  # Order by most recent uploads

    def __str__(self):
        return self.title


    
   