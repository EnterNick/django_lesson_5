from django.db import models
from django.contrib.auth import get_user_model

from datetime import datetime


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ManyToOneRel('author', get_user_model(), 'author', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f'comment, author: {self.author.username}'
