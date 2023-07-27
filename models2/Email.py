from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class EmailConfirmation(models.Model):
    email = models.EmailField(unique=True)
    key = models.CharField(max_length=64, unique=False)
    created_at = models.DateTimeField(default=timezone.now)