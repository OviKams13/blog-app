from django.db import models
from datetime import datetime

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    author = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=datetime.now, blank=True)