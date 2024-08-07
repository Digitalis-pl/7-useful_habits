from rest_framework.validators import ValidationError

from django.shortcuts import get_object_or_404

from habits.models import Habit

from datetime import timedelta


class PrizeOrPleasureHabitValidator:
    def __init__(self, associated_habit, prize, is_pleasant):
        self.associated_habit = associated_habit
        self.prize = prize
        self.is_pleasant = is_pleasant

    def __call__(self, value):
        is_pleasant_flag = dict(value).get(self.is_pleasant)
        prize = dict(value).get(self.prize)
        associated_habit = dict(value).get(self.associated_habit)
        if is_pleasant_flag:
            if prize or associated_habit:
                raise ValidationError(f'Это приятная привычка, не стоит награждать за награду, необходим баланс')
        elif not is_pleasant_flag:
            habit = get_object_or_404(Habit, pk=associated_habit.pk)
            if not habit.is_pleasant:
                raise ValidationError(f"После выполнения обещания стоит себя наградить,"
                                      f" а привычка {habit.action} не является приятной")
            elif prize and associated_habit:
                raise ValidationError("Может быть либо приятная привычка, либо приз")


class TimeValidator:
    def __init__(self, time):
        self.time = time

    def __call__(self, value):
        time = dict(value).get(self.time)
        time_td = timedelta(minutes=time.minute, seconds=time.second)
        totalsecond = time_td.total_seconds()
        if totalsecond > 120:
            raise ValidationError(f'Слишком долго для небольшой привычки.')


class PeriodOfHabitValidator:
    pass
