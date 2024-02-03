from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png", blank=True)
    author = models.ForeignKey(User, default=None, on_delete = models.CASCADE)
    # add in thumbnail later
    # add in author later
    def __str__(self):
        return self.title
    # making a snippet for the body
    def snippet(self):
        return self.body[:50] +"..."