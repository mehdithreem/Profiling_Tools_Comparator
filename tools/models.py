from django.db import models

# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100)
    version = models.CharField(max_length=10)

    scores = models.ManyToManyField(
        'criteria.Criteria',
        through='criteria.CriteriaScore',
        through_fields=('tool', 'criteria'),
    )

    tasks_scores = models.ManyToManyField(
        'tasks.Task',
        through='tasks.TaskScore',
        through_fields=('tool', 'task'),
    )

    def __str__(self):
        return self.name +  ' (v' + self.version + ')'