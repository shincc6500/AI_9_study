from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


# class Posts(models.Model):
#     title = models.CharField(max_length = 200)
#     content = models.TextField()
    
#     create_date = models.DateTimeField(auto_now_add=True)
#     edited_date = models.DateTimeField(auto_now = True)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Post")
#     def __str__(self):
#         return self.title