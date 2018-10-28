from django.contrib import admin

# Register your models here.
from sdlc_proto.criteria.models import CriteriaScore
from sdlc_proto.tasks.models import TaskScore
from sdlc_proto.tools.models import Tool


class CriteriaScoreInline(admin.TabularInline):
    model = CriteriaScore
    extra = 0

class TaskScoreInline(admin.TabularInline):
    model = TaskScore
    extra = 0


class ToolAdmin(admin.ModelAdmin):
    inlines = (CriteriaScoreInline, TaskScoreInline,)
    exclude = ('scores',)


admin.site.register(Tool, ToolAdmin)
# TODO: fix nested admin