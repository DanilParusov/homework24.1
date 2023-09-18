from django.urls import path, include
from rest_framework import routers
from . import views
from .views import UserCreateApiView


urlpatterns = [
    path('create/', UserCreateApiView.as_view(), name='user_create'),
]
