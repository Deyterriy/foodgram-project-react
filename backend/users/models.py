from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import LENGTH


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(
        verbose_name="username", max_length=LENGTH.l_150, unique=True
    )
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=LENGTH.l_150,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=LENGTH.l_150,
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribing',
        verbose_name='Подписан'
    )

    class Meta:
        verbose_name = 'Подписка на авторов'
        verbose_name_plural = 'Подписки на авторов'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscribe'
            )
        ]

    def __str__(self):
        return f'{self.user.username} - {self.author.username}'
