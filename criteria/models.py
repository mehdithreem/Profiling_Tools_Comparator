from django.db import models

# Create your models here.
from tools.models import Tool


class Criteria(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    benefits = models.IntegerField(default=0)
    hurts = models.IntegerField(default=0)
    parent = models.ForeignKey('Criteria', on_delete=models.CASCADE, null=True, blank=True)

    category = models.CharField(max_length=150, null=True)

    def __str__(self):
        return '[' + str(self.pk) + '] [' + str(self.category) + '] ' + self.name + ' -'

class CriteriaScore(models.Model):
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)

    score = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = (('criteria', 'tool'),)

    def __str__(self):
        return '[' + self.tool.name + '] '  + str(self.score) + '  in:' + self.criteria.name