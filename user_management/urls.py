from django.urls import path
from .views import ProfileUpdate

urlpatterns = [
    path('<str:username>', ProfileUpdate.as_view(), name='update'),
]

app_name = 'user_management'