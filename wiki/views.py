from django.views.generic import ListView, DetailView
from .models import Article, ArticleCategory


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'wiki_list.html'
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki_detail.html'