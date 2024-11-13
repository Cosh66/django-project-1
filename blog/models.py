from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # Assuming a Post model exists with at least a title and content
    title = models.CharField(max_length=200)
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='commenter'
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
   