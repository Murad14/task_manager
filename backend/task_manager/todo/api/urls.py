'''
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, PhotoViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
'''
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TaskViewSet, PhotoViewSet

router = SimpleRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('photo/', PhotoViewSet.as_view({'get': 'list', 'post': 'create'}), name='photo-list'),
    path('photo/<int:pk>/', PhotoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='photo-detail'),
]
