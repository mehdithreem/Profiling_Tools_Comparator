from django.contrib import admin

# Register your models here.
from sdlc_proto.tasks.models import Task, TaskScore

admin.site.register(Task)
admin.site.register(TaskScore)