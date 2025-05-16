from django.urls import path
from .views import home_list


urlpatterns = [
    path('', home_list, name='home')
]

app_name = "home"
