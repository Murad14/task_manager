from django.contrib import admin
from django.urls import path, include
from todo.api.views import TaskListCreateView, TaskRetrieveUpdateDestroyView, PhotoListCreateView, PhotoRetrieveUpdateDestroyView
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.api.urls')),
    path('api/todo/', include('todo.api.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
