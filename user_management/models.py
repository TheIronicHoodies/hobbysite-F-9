from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse #filler

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=63)
    email_address = models.EmailField()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('home') #temporary fix set this to home url
    