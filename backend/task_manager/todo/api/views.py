from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TaskSerializer, PhotoSerializer
from ..models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = PhotoSerializer