from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from .models import Article
from .forms import ArticleCreateForm, ArticleUpdateForm, CommentForm
from collections import defaultdict

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'blog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user_profile = getattr(self.request.user, "profile", None)
        else:
            user_profile = None

        if user_profile:
            user_articles  = Article.objects.filter(author=user_profile)
            other_articles = Article.objects.exclude(author=user_profile)
        else:
            user_articles  = Article.objects.none()          # empty queryset
            other_articles = Article.objects.all()

        grouped_articles = defaultdict(list)
        for article in other_articles.select_related("category"):
            category_name = article.category.name if article.category else "Uncategorized"
            grouped_articles[category_name].append(article)

        grouped_articles = dict(sorted(grouped_articles.items(), key=lambda item: item[0].lower()))

        context["user_articles"]   = user_articles
        context["grouped_articles"] = grouped_articles
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog_detail.html'
    #context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['form'] = CommentForm()
        context['comments'] = article.comments.order_by('-created_on')
        context['author_articles'] = Article.objects.filter(
            author=article.author
        ).exclude(pk=article.pk)[:2]
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.author = request.user.profile  
            comment.save()
            return self.get(request, *args, **kwargs)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'blog_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile  
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'blog_update.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user.profile:
            return HttpResponseForbidden("You are not allowed to edit this article.")
        return super().dispatch(request, *args, **kwargs)