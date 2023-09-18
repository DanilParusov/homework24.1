from django.shortcuts import render
from rest_framework import generics

from users.serializers import UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserSerializer
