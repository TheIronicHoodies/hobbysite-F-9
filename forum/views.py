from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, "forum/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "forum/post_detail.html", {"post": post})

