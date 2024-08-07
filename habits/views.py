from rest_framework import generics

from django.shortcuts import render

from habits.models import Habit
from habits.permissions import IsOwner, OrdinaryUser
from habits.serializers import HabitSerializer
from habits.paginators import CustomPagination

# Create your views here.


class HabitCreateAPI(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner, OrdinaryUser)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class NotMyHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Habit.objects.filter(is_published=True)

class HabitUpdateAPI(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitDeleteAPI(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)
