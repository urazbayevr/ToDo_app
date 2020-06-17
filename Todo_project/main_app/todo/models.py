from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cutoff_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')
