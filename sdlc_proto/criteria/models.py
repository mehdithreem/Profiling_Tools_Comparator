from abc import abstractmethod

from django.db import models

from sdlc_proto.tools.models import Tool


class Criteria(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    benefits = models.FloatField(default=0.0)
    hurts = models.FloatField(default=0.0)
    parent = models.ForeignKey('Criteria', on_delete=models.CASCADE, null=True, blank=True)

    inspiredFrom = models.CharField(max_length=250, null=True, blank=True)

    SCORE_MODE_CHOICES = (
        ('0', 'Only Use Children'),
        ('1', 'Include Self Score')
    )

    score_mode = models.CharField(max_length=1, choices=SCORE_MODE_CHOICES, default='0')

    def __str__(self):
        return self.name + ' [' + str(self.pk) + ']'


class CriteriaScore(models.Model):
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)

    score = models.FloatField(default=0.0)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = (('criteria', 'tool'),)

    def __str__(self):
        return '[' + self.tool.name + '] '  + str(self.score) + '  in:' + self.criteria.name

    @staticmethod
    def getAll():
        return CriteriaScore.objects.all()

    @staticmethod
    def getByCriteria(criteria_id):
        scores = CriteriaScore.objects.filter(criteria__pk=criteria_id)

        scoreMap = {}
        for score in scores:
            scoreMap[score.tool.pk] = score

        return scoreMap


class CriteriaDisplayNode():
    def __init__(self, _criteria, depth=0):
        self.criteria = _criteria
        self.children = []
        self.leafCount = 0
        self.height = 0
        self.depth = 0
        self.scores = {}

        if (depth):
            self.depth = depth

        self.scores = CriteriaScore.getByCriteria(_criteria.pk)

    @abstractmethod
    def getRowGroups(self):
        pass

    @abstractmethod
    def preOrderTraverse(self, rowGroup):
        pass

    @abstractmethod
    def isSelfScore(self):
        pass


class RealCriteriaDisplayNode(CriteriaDisplayNode):
    def __init__(self, _criteria, depth=0):
        super().__init__(_criteria, depth)

        for child in Criteria.objects.filter(parent__exact=self.criteria):
            tempChild = RealCriteriaDisplayNode(child, self.depth + 1)
            self.children.append(tempChild)
            self.leafCount += tempChild.leafCount if len(tempChild.children) > 0 else 1
            self.height = max(self.height, tempChild.height + 1)

        # if self score
        if (self.children and self.criteria.score_mode == '1'):
            self.children.append(FakeCriteriaDisplayNode(self.criteria, self.depth + 1))
            self.leafCount += 1


    def getRowGroups(self):
        rowGroup = [[]]
        self.preOrderTraverse(rowGroup)
        return rowGroup

    def preOrderTraverse(self, rowGroup):
        rowGroup[-1].append(self)

        if (len(self.children) > 0):
            self.children[0].preOrderTraverse(rowGroup)

        for child in self.children[1:]:
            rowGroup.append([])
            child.preOrderTraverse(rowGroup)

    def isSelfScore(self):
        return False


class FakeCriteriaDisplayNode(CriteriaDisplayNode):
    def __init__(self, _criteria, depth):
        super().__init__(_criteria, depth)

    def getRowGroups(self):
        return []

    def preOrderTraverse(self, rowGroup):
        rowGroup[-1].append(self)

    def isSelfScore(self):
        return True
