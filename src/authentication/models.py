from django.db import models

# src/accounts/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

