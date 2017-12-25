from django.contrib import admin

# Register your models here.
from criteria.models import CriteriaScore
from tasks.models import TaskScore
from tools.models import Tool


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