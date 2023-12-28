from django.contrib import admin
from django.urls import path, include
from todo .api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, 'task')    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.api.urls')),
    path('api/todo/', include(router.urls)),
]
