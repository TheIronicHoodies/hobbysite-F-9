from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'forum_list.html'
    context_object_name = 'posts'  

class PostDetailView(DetailView):
    model = Post
    template_name = 'forum_detail.html'
    context_object_name = 'post'  