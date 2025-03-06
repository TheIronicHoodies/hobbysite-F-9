from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

def forum_list(request):
    posts = Post.objects.all()
    return render(request, "forum/forum_list.html", {"posts": posts})

def forum_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "forum/forum_detail.html", {"post": post})

