# 在 api 应用的 urls.py 文件中定义路由

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TopicsViewSet

from django.urls import path
from . import views
router = DefaultRouter()
router.register(r'api/topics', TopicsViewSet)

urlpatterns = [
    path('', include(router.urls)),


    path('api/server-timestamp/', views.get_server_timestamp, name='get_server_timestamp'),
]
