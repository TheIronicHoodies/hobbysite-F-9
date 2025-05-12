from .models import Post
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Thread, ThreadCategory, Comment
from .forms import ThreadForm, CommentForm

def thread_list(request):
    categories = ThreadCategory.objects.all()

    user_threads = []
    other_threads = Thread.objects.all()

    if request.user.is_authenticated:
        user_threads = Thread.objects.filter(author=request.user.profile)
        other_threads = other_threads.exclude(author=request.user.profile)

    return render(request, "forum/thread_list.html", {"categories": categories, "user_threads": user_threads, "other_threads": other_threads})


def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk).first()
    comments = Comment.objects.filter(thread=thread)

    related_threads = Thread.objects.filter(category=thread.category).exclude(pk=pk)[:2]

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user.profile
            comment.thread = thread
            comment.created_on = timezone.now()
            comment.save()
            return redirect("forum:thread_detail", pk=thread.pk)
    else:
        comment_form = CommentForm()

    return render(request, "forum/thread_detail.html", {"thread": thread, "comments": comments, "related_threads": related_threads, "comment_form": comment_form})

@login_required
def add_thread(request):

@login_required
def edit_thread(request, pk):