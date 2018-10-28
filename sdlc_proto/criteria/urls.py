from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.compareAll, name='compareAll'),
    path('update', views.updateCriteria, name='updateCriteria'),
    path('score', views.scoreCriteria, name='scoreCriteria'),
]