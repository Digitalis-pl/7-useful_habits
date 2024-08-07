from rest_framework import generics

from django.shortcuts import render

from users.models import User
from users.serializers import UserSerializer

# Create your views here.


class UserCreateAPI(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserListViewAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserViewAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPI(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPI(generics.DestroyAPIView):
    queryset = User.objects.all()
