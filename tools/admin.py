from django.contrib import admin

# Register your models here.
from criteria.models import CriteriaScore
from tools.models import Tool


class CriteriaScoreInline(admin.TabularInline):
    model = CriteriaScore
    extra = 0

class ToolAdmin(admin.ModelAdmin):
    inlines = (CriteriaScoreInline,)
    exclude = ('scores',)


admin.site.register(Tool, ToolAdmin)
# TODO: fix nested admin