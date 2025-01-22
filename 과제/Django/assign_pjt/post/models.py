from django.db import models
from django.conf import settings

class Posts(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    
    create_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Post")
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
  

