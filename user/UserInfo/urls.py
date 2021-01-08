from django.urls import path

from .views import UserViewSet, UserAPIView

urlpatterns = [
    path('users', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('users/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })), 
    path('user', UserAPIView.as_view())
]
