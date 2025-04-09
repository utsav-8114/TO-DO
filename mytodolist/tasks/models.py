from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    marked = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True)
    reminder_time = models.DateTimeField(null=True,blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=False)
    def __str__(self):
        return self.title