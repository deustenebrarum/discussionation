from django.db import models
from django.contrib.auth.models import User
import re


class Topic(models.Model):
    title = models.CharField(
        max_length=100, blank=False, verbose_name='название'
    )
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'темы'
        verbose_name = 'тема'


class Application(models.Model):
    class Type(models.IntegerChoices):
        REFERENCE = 0
        IMAGE = 1
        VIDEO = 2

    FOLDER_NAME = 'uploads'
    UPLOAD_PATH = f'{FOLDER_NAME}/%Y/%m/%d/'
    application_type = models.IntegerField(
        choices=Type.choices,
        null=False,
        verbose_name='тип',
    )
    application_file = models.FileField(
        null=True, blank=True,
        upload_to=UPLOAD_PATH,
        verbose_name='файл',
    )

    def __str__(self):
        return re.sub(
            fr'.*{self.FOLDER_NAME}', '',
            self.application_file.path
        )

    class Meta:
        verbose_name_plural = 'приложения'
        verbose_name = 'приложение'


class Post(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL,
        null=True, verbose_name='тема'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, verbose_name='пользователь')
    content = models.TextField(blank=False, verbose_name='содержание')
    application = models.ForeignKey(
        Application, on_delete=models.SET_NULL, null=True, verbose_name='приложение'
    )
    tags = models.ManyToManyField("Tag", verbose_name='теги', blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='дата обновления')

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=False, verbose_name='пост')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name='пользователь')
    content = models.TextField(blank=False, verbose_name='содержание')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='дата обновления')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Tag(models.Model):
    title = models.CharField(
        max_length=100, blank=False,
        unique=True,
        verbose_name='название'
    )
    posts = models.ManyToManyField(
        Post, verbose_name='посты', blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'теги'
        verbose_name = 'тег'
