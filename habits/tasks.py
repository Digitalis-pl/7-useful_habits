import json

from django.core import serializers

from celery import shared_task

from habits.models import Habit
from users.models import User

from datetime import datetime, timedelta

from .services import send_message_in_tg


@shared_task
def form_today_data():
    today = datetime.now().strftime('%Y-%m-%d')
    habits = Habit.objects.filter(period='every_day') | Habit.objects.filter(next_day_to_do=today)
    for habit in habits:
        if habit.period == 'every_week':
            habit.next_day_to_do = datetime.now() + timedelta(days=7)
            habit.save()
    js_habits = Habit.objects.filter(period='every_day') | Habit.objects.filter(next_day_to_do=today)
    js_data = serializers.serialize('json', js_habits)

    with open('today_data/today_habit.json', 'w', encoding='utf-8') as f:
        json.dump(js_data, f)


@shared_task
def send_message():
    with open('today_data/today_habit.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        dict_data = json.loads(data)
        for habit in dict_data:
            habit_time = datetime.strptime(habit['fields']['time'], '%H:%M:%S')
            if datetime.strftime(habit_time, '%H:%M:%S') == datetime.now().strftime('%H:%M:%S'):
                send_message_in_tg(chat_id=User.objects.get(pk=habit.user),
                                   message=f'пора выполнить привычку {habit.action}')
