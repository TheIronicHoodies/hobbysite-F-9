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
    template_name = "forum_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = ThreadCategory.objects.all()

        context["categories"] = categories

        if self.request.user.is_authenticated:
            user_threads = Thread.objects.filter(author=self.request.user.profile)
        else:
            user_threads = Thread.objects.none()

        context["user_threads"] = user_threads

        # Group other threads by category
        threads_by_category = []
        for category in categories:
            threads = Thread.objects.filter(category=category)
            threads_by_category.append((category, threads))

        context["threads_by_category"] = threads_by_category

        return context
    
class ThreadDetailView(DetailView):
    model = Thread
    template_name = "forum_detail.html"
    context_object_name = "thread"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = self.get_object()

        context["comments"] = Comment.objects.filter(thread=thread)
        context["related_threads"] = Thread.objects.filter(category=thread.category).exclude(pk=thread.pk)[:2]

        context["comment_form"] = kwargs.get("comment_form", CommentForm())
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = self.object
            comment.author = request.user.profile 
            comment.created_on = timezone.now()
            comment.save()
            return redirect("forum:thread_detail", pk=self.object.pk)
        else:
            context = self.get_context_data(comment_form=form)
            return self.render_to_response(context)

class ThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = "add_thread.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("forum:thread_detail", kwargs={"pk": self.object.pk})



class ThreadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = "add_thread.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        thread = self.get_object()
        return self.request.user.profile == thread.author

    def get_success_url(self):
        return reverse("forum:thread_detail", kwargs={"pk": self.object.pk})
