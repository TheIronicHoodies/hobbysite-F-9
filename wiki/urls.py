from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ImageCreateView

urlpatterns = [
    path('articles/list', ArticleListView.as_view(), name='list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('article/add', ArticleCreateView.as_view(), name='create'),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view(), name='update'),
    path('article/gallery/add', ImageCreateView.as_view(), name='gallery')
]

app_name = "wiki"