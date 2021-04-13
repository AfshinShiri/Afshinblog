from django.db import models
from django.contrib.auth.models import User


class comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):

        return self.name

    def snippet(self):
        return self.body[0]+'...'

# Create your models here.
