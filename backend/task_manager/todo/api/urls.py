from django.urls import path
from .views import TaskListCreateView,TaskCreateView, TaskRetrieveUpdateDestroyView, PhotoListCreateView, PhotoRetrieveUpdateDestroyView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('photos/', PhotoListCreateView.as_view(), name='photo-list'),
    path('photos/<int:task_id>/', PhotoRetrieveUpdateDestroyView.as_view(), name='photo-detail'),
]
