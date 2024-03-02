from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    username = models.CharField(max_length=15, verbose_name="имя", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
