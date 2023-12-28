from django.contrib import admin
from .models import Task #Photo

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'is_complete', 'created_at', 'updated_at', 'creator')
    list_filter = ('priority', 'is_complete', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

'''
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('task', 'image', 'uploaded_at')
    list_filter = ('task', 'uploaded_at')
'''

