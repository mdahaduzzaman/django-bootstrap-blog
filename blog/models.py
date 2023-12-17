from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likedBy = models.ManyToManyField(User, related_name='likedBy')
    dislikedBy = models.ManyToManyField(User, related_name="dislikedBy")

    def __str__(self) -> str:
        return self.title

