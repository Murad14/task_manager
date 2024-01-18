from django.urls import path
from .views import TaskCreateView, TaskRetrieveUpdateDestroyView, PhotoListCreateView, PhotoRetrieveUpdateDestroyView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('photos/', PhotoListCreateView.as_view(), name='photo-list'),
    path('photos/<int:task_id>/', PhotoRetrieveUpdateDestroyView.as_view(), name='photo-detail'),
]
