from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Thread, ThreadCategory, Comment
from .forms import ThreadForm, CommentForm

class ThreadListView(ListView):
    model = Thread
    template_name = "forum/thread_list.html"
    context_object_name = "other_threads"

    user_threads = []
    other_threads = Thread.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ThreadCategory.objects.all()

        if self.request.user.is_authenticated:
            context["user_threads"] = Thread.objects.filter(author=self.request.user.profile)
            context["other_threads"] = Thread.objects.exclude(author=self.request.user.profile)
        else:
            context["user_threads"] = []

        return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = "forum/thread_detail.html"
    context_object_name = "thread"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = self.get_object()

        context["comments"] = Comment.objects.filter(thread=thread)
        context["related_threads"] = Thread.objects.filter(category=thread.category).exclude(pk=thread.pk)[:2]

        if self.request.method == "POST":
            comment_form = CommentForm(self.request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = self.request.user.profile
                comment.thread = thread
                comment.created_on = timezone.now()
                comment.save()
                return redirect("forum:thread_detail", pk=thread.pk)
        else:
            comment_form = CommentForm()

        context["comment_form"] = comment_form
        return context


class ThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = "forum/add_thread.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("forum:thread_detail", kwargs={"pk": self.object.pk})



class UpdateThreadView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = "forum/add_thread.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        thread = self.get_object()
        return self.request.user.profile == thread.author

    def get_success_url(self):
        return reverse("forum:thread_detail", kwargs={"pk": self.object.pk})