from rest_framework import serializers
from habits.models import Habit
from habits.validators import TimeValidator, PrizeOrPleasureHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [TimeValidator(time="time_to_do"),
                      PrizeOrPleasureHabitValidator(associated_habit="associated_habit",
                                                    prize="prize",
                                                    is_pleasant="is_pleasant"),
                      ]
