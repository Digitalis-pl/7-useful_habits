from django.contrib import admin

from habits.models import Habit

# Register your models here.


@admin.register(Habit)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "action", "place", "time", "is_pleasant",
                    "associated_habit", "period", "prize", "time_to_do",
                    "is_published")
