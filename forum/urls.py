from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("threads/", PostListView.as_view(), name="thread-list"),
    path("thread/1/", PostDetailView.as_view(), name="thread-detail"),
]

app_name = "forum"
