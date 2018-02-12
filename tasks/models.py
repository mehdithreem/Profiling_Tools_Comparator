from django.db import models

# Create your models here.
from tools.models import Tool


class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    pre = models.TextField(blank=True)

    def __str__(self):
        return '[' + str(self.pk) + '] ' + self.name

class TaskScore(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)

    how = models.TextField()
    num_of_steps = models.IntegerField(default=0)
    ease_score = models.IntegerField(default=0)
    quality_score = models.IntegerField(default=0)
    pre = models.TextField(blank=True)

    class Meta:
        unique_together = (('task', 'tool'),)

    def __str__(self):
        return '[' + self.tool.name + '] task:' + '#' + str(self.task.id) + self.task.name