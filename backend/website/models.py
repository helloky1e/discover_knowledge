from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    introduction = models.TextField()
    contact = models.CharField(max_length=200)
    work_experience = models.TextField()

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
