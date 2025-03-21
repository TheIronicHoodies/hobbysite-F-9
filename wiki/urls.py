from django.urls import path

from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('articles/list', ArticleListView.as_view(), name='list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
]

app_name = "wiki"