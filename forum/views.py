from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'forum_list.html'
    context_object_name = 'posts'  # Allows template to use `posts` instead of `object_list`

class PostDetailView(DetailView):
    model = Post
    template_name = 'forum_detail.html'
    context_object_name = 'post'  # Allows template to use `post` instead of `object`