from django.http import HttpResponse
from django.shortcuts import render

from criteria.models import Criteria, RealCriteriaDisplayNode, CriteriaScore
from tools.models import Tool


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class Tools(object):
    pass


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