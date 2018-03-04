from django.apps import AppConfig
from django import template

register = template.Library()

class CommonTagsConfig(AppConfig):
    name = 'common_tags'
