from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(index):
    return HttpResponse("Hello, world. You're at the tools index.")