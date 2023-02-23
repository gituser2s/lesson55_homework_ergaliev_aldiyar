from django.contrib import admin
from webapp.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'title', 'description', 'detailed_description', 'date', 'created_at')
    list_filter = ('id', 'status', 'title', 'description', 'detailed_description', 'date', 'created_at')
    search_fields = ('status', 'title', 'description', 'detailed_description', 'date')
    fields = ('status', 'title', 'description', 'detailed_description', 'date', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at', 'deleted_at', 'is_deleted')


admin.site.register(Task, TaskAdmin)
