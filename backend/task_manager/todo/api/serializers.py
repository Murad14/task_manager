from rest_framework import serializers
from ..models import Task, Photo

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'due_date',
            'priority',
            'is_complete',
            'created_at',
            'updated_at',
            'creator',
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'creator',)

class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = (
            'id',
            'task',
            'image',
            'uploaded_at',
        )
        read_only_fields = ('id', 'uploaded_at',)