from django.urls import path
from .views import post_list, post_detail

urlpatterns = [
    path("threads/", post_list, name="thread-list"),
    path("thread/<int:pk>/", post_detail, name="thread-detail"),
]

app_name = "forum"
