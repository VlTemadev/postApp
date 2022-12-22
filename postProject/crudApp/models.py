from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    userPost = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Post by", default="", null=True)
    content = models.TextField('Контент')
    postDate = models.DateTimeField('Дата публикации', default=datetime.now)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("postDetail", args=[self.pk])

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

