"""Sets list and detail view of forum's list and detail view."""

from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    """List view for listing all available posts."""

    model = Post
    template_name = 'forum_list.html'
    context_object_name = 'posts'  

class PostDetailView(DetailView):
    """Detail view for listing the details of a post."""

    model = Post
    template_name = 'forum_detail.html'
    context_object_name = 'post'  