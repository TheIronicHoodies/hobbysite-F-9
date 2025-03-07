"""Sets paths to forum's list and detail view."""

from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("threads/", PostListView.as_view(), name="thread-list"),
    path("thread/<int:pk>/", PostDetailView.as_view(), name="thread-detail"),
]

app_name = "forum"
