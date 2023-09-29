from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}
# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=30, verbose_name='номер', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

