from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.email