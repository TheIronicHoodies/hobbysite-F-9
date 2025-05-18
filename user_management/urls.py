from django.urls import path
from .views import ProfileCreate, ProfileUpdate

urlpatterns = [
    path('register', ProfileCreate.as_view(), name='register'),
    path('<str:username>', ProfileUpdate.as_view(), name='update'),
]

app_name = 'user_management'