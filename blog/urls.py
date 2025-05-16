from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns= [
    path('', ArticleListView.as_view(), name='blog_list'),
    path('blog/articles', ArticleListView.as_view(), name='blog_list'),
    path('blog/article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('blog/article/add', ArticleCreateView.as_view(), name='blog_create'),
    path('blog/article/<int:pk>/edit', ArticleUpdateView.as_view(), name='blog_update')
]

app_name = "blog"
