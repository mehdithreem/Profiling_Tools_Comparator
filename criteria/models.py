from django.db import models

# Create your models here.
from tools.models import Tool


class Criteria(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    benefits = models.FloatField(default=0.0)
    hurts = models.FloatField(default=0.0)
    parent = models.ForeignKey('Criteria', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '[' + str(self.pk) + '] ' + self.name + ' -'

class CriteriaScore(models.Model):
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)

    score = models.FloatField(default=0.0)
    notes = models.TextField(blank=True)

    SCORE_MODE_CHOICES = (
        ('0', 'From Children'),
        ('1', 'No Children'),
        ('2', 'Use Both'),
    )

    score_mode = models.CharField(max_length=1, choices=SCORE_MODE_CHOICES, default='0')

    class Meta:
        unique_together = (('criteria', 'tool'),)

    def __str__(self):
        return '[' + self.tool.name + '] '  + str(self.score) + '  in:' + self.criteria.name