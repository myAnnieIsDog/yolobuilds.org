from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class License(models.Model):
    group = models.CharField(max_length=7)
    description = models.CharField(max_length=55)
