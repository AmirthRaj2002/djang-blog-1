from urllib import request
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, default="")
    author=models.ForeignKey(User,default="Anonymous",on_delete=models.CASCADE,)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(default=datetime(2022,1,1))

    def __str__(self):
        return self.title
    class Meta:
        ordering = ("-created_at", "-updated_at", "title", "author")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(default='Anonymous',max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.author} says: {self.content}"

    class Meta:
        ordering = ("-created_at", "-edited_at", "author","id")
