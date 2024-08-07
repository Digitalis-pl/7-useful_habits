from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
null_options = {'blank': True, 'null': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, )
    phone = models.CharField(max_length=35, verbose_name='телефон', **null_options)
    city = models.CharField(max_length=100, verbose_name='Город', **null_options)

    tg_chat_id = models.CharField(max_length=100,
                                  verbose_name='Телеграм чат (ID)',
                                  **null_options)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
