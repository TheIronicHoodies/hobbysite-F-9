from django.urls import path
from .views import ProfileUpdate

urlpatterns = [
    path('profile/username', ProfileUpdate.as_view(), name='profile'),
]

app_name = 'user_management'