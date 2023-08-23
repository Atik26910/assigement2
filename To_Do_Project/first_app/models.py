# Create your models here.
from django.db import models

class TaskModel(models.Model):
    task_Title = models.CharField(max_length=100)
    task_Description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle