from rest_framework import generics
from ..models import Task, Photo
from .serializers import TaskSerializer, PhotoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def post (self, request, *args, **kwargs):
        print("Received Data:", self.request.data) # type: ignore
        serializers = self.get_serializer(data=request.data) 
        
        if serializers.is_valid():
            print("Validated Data:", serializers.validated_data) 
            if request.data['image'] == '':
                serializers.validated_data['image'] = '/default_images/default-image.jpg'
            serializers.save(creator=self.request.user)   
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    
    def perform_create(self, serializer):
        # Ensure 'task' and 'image' are present in the request data
        print("Received Data:", self.request.data) # type: ignore
        task_id = self.request.data.get('id') # type: ignore
        image = self.request.data.get('image') # type: ignore

        # Ensure task_id is not None and exists in the Task model
        try:
            task = Task.objects.get(pk=task_id)
            serializer.save(task=task, image=image)
        except Task.DoesNotExist:
            # Handle the case where the task_id is not valid
            print("Task does not exist!")
            raise serializers.ValidationError("Invalid task ID") 
class PhotoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    lookup_field = 'task_id'
    
    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        print("Task ID from URL:", task_id)
        queryset = Photo.objects.filter(task_id=task_id)
        print("Queryset:", queryset)  # Debug print
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)  # Use Response instead of returning the instance directly

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    