from django.db import models

# Create your models here.
class Task(models.Model):
    user_id = models.AutoField(primary_key=True)
    name_task = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(default='')

    def __str__(self):
        return f'task: {self.name_task}'