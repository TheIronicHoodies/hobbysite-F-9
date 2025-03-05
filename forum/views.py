from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_on')  
    return render(request, "forum/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = Post.objects.filter(pk=pk).first()
    return render(request, "forum/post_detail.html", {"post": post})

