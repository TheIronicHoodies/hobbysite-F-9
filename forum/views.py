from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, "forum/post_list.html", {"posts": posts})

def post_detail(request):
    post = Post.objects.all() 
    return render(request, "forum/post_detail.html", {"post": post})

