from rest_framework import serializers
from ..models import Task, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'uploaded_at')
        read_only_fields = ('id', 'uploaded_at')

class TaskSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

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
            'photos',
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'creator', 'photos')
'''
    def create(self, validated_data):
        # Allow creating nested photos during task creation
        photos_data = validated_data.pop('photos', [])
        print("Photos data:", photos_data)
        # Automatically set the creator field to the currently logged-in user
        validated_data['creator'] = self.context['request'].user

        # Extract fields from validated_data
        task_instance = Task.objects.create(**validated_data)

        for photo_data in photos_data:
            # Link each photo to the created task
            Photo.objects.create(task=task_instance, **photo_data)

        return task_instance

'''