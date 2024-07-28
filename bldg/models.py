import datetime


from django.db import models
from django.utils import timezone


class Permit(models.Model):
    date = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.number
    
    def applied_within_30_days(self):
        return self.date >= timezone.now() - datetime.timedelta(days=30)




