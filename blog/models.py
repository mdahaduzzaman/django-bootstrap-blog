from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = RichTextField()
    image = models.ImageField(upload_to='Post-Images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likedBy = models.ManyToManyField(User, related_name='likedBy', blank=True)
    dislikedBy = models.ManyToManyField(User, related_name="dislikedBy", blank=True)

    def __str__(self) -> str:
        return self.title

