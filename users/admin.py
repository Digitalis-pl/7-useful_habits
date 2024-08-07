from django.contrib import admin

from users.models import User

# Register your models here.


@admin.register(User)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
