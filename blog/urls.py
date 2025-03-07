from django.urls import path

from .views import ArticleListView, ArticleDetailView

urlpatterns= [
    path('', ArticleListView.as_view(), name='blog_list'),
    path('blog/articles', ArticleListView.as_view(), name='blog_list'),
    path('blog/article/<int:pk>', ArticleDetailView.as_view(), name='blog_detail'),
]

app_name = "blog"