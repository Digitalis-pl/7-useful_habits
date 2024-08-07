import datetime

from django.db import models
from users.models import User


# Create your models here.

null_option = {'blank': True, 'null': True}


class Habit(models.Model):

    PERIOD_CHOICES = [
        ("every_day", "Ежедневно"),
        ("every_week", "Еженедельно"),
    ]

    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             verbose_name='Автор',
                             related_name='user',
                             **null_option)

    action = models.CharField(max_length=250,
                              verbose_name='Действие',
                              help_text='Что вы будете делать')

    place = models.CharField(max_length=250,
                             verbose_name='Где Вы будете делать')

    time = models.TimeField(default=datetime.datetime.now().strftime("%H:%M:%S"))

    is_pleasant = models.BooleanField(verbose_name='отметка для приятной привычки')

    associated_habit = models.ForeignKey('self',
                                         on_delete=models.SET_NULL,
                                         **null_option)

    period = models.CharField(max_length=100,
                              verbose_name='Периодичность',
                              help_text='Периодичность',
                              choices=PERIOD_CHOICES,
                              default='every_day')

    next_day_to_do = models.DateField(verbose_name='день выполнения', **null_option)

    prize = models.CharField(max_length=250,
                             verbose_name='Награда',
                             help_text='Награда за соблюдение',
                             **null_option)

    time_to_do = models.TimeField(verbose_name='Время на выполнение привычки',
                                  help_text='время на выполнение')

    is_published = models.BooleanField(verbose_name='Публичность')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
