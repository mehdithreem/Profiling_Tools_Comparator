from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render

from sdlc_proto.criteria.models import Criteria, RealCriteriaDisplayNode, CriteriaScore
from sdlc_proto.tools.models import Tool


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def compareAll(request):
    nodes = []
    treeHeight = 0
    for c in Criteria.objects.filter(parent__isnull=True):
        tempNode = RealCriteriaDisplayNode(c)
        nodes.append(tempNode)
        treeHeight = max(treeHeight, tempNode.height)

    rowGroups = []
    for n in nodes:
        rowGroups.extend(n.getRowGroups())

    toolsList = Tool.objects.all()

    return render(request, "compare.html", {
        'rowGroup': rowGroups,
        'treeHeight': treeHeight,
        'tools': toolsList
    })

@login_required
def updateCriteria(request):
    pk = request.POST['pk']
    description = request.POST['description']
    inspiredFrom = request.POST['inspiredFrom']
    benefits = request.POST['benefits']
    hurts = request.POST['hurts']

    target = Criteria.objects.get(pk=pk)

    target.description = description
    target.inspiredFrom = inspiredFrom
    target.benefits = benefits
    target.hurts = hurts

    target.save()

    return HttpResponse(True)

@login_required
def scoreCriteria(request):
    toolId = request.POST['toolId']
    criteriaId = request.POST['criteriaId']
    score = request.POST['score']
    notes = request.POST['notes']

    criteria = Criteria.objects.get(pk=criteriaId)
    tool = Tool.objects.get(pk=toolId)

    try:
        target = CriteriaScore.objects.get(criteria=criteria, tool=tool)
        target.score = score
        target.notes = notes
    except ObjectDoesNotExist:
        target = CriteriaScore(
            criteria=criteria,
            tool=tool,
            score=score,
            notes=notes)
    target.save()

    return HttpResponse(True)

