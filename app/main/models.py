from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model): 
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()


class Application(models.Model):
    class Type(models.IntegerChoices):
        REFERENCE = 0
        IMAGE = 1
        VIDEO = 2

    id = models.IntegerField(primary_key=True)
    application_type = models.IntegerField(
        choices=Type.choices,
        null=False
    )


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL,
        null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    content = models.TextField(blank=False)
    application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("Tag", through="PostTag")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    posts = models.ManyToManyField(
        Post, through="PostTag",
    )


class PostTag(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False)
