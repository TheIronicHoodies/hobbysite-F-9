from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(User):
    name = models.CharField(max_length=63, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}'
