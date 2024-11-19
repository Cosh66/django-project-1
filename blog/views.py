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
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )


