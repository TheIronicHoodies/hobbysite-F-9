from django.urls import path
from .views import forum_list, forum_detail

urlpatterns = [
    path("threads/", forum_list, name="thread-list"),
    path("thread/<int:pk>/", forum_detail, name="thread-detail"),
]

app_name = "forum"
