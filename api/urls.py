# 在 api 应用的 urls.py 文件中定义路由

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TopicsViewSet

router = DefaultRouter()
router.register(r'api', TopicsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
