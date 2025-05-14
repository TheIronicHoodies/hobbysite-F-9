from django.urls import path
from .views import ThreadDetailView, ThreadListView, ThreadCreateView, ThreadUpdateView

urlpatterns = [
    path("threads/", ThreadListView.as_view(), name="thread-list"),
    path("thread/<int:pk>/", ThreadDetailView.as_view(), name="thread-detail"),
    path("thread/add/", ThreadCreateView.as_view(), name="add-thread"),
    path("thread/<int:pk>/edit/", ThreadUpdateView.as_view(), name="edit-thread"),
]

app_name = "forum"
