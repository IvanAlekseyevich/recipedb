from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='электронная почта',
        max_length=254,
        unique=True
    )
    username = models.CharField(
        verbose_name='логин',
        max_length=150,
        unique=True,
        db_index=True
    )
    password = models.CharField(
        verbose_name='пароль',
        max_length=150
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=150
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=150
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscription(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribers',
        verbose_name='автор'
    )
    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='signed',
        verbose_name='подписчик'
    )

    class Meta:
        ordering = ['author']
        verbose_name_plural = 'Подписки'
