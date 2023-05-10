from django.db import models
import datetime

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateField(default=datetime.date.today)
    date_updated = models.DateField(default=datetime.date.today)
    completed = models.BooleanField(default=False)
