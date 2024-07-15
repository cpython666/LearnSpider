# 在 api 应用的 views.py 文件中定义视图类

from rest_framework import viewsets
from topics.models import Topics
from topics.serializers import TopicsSerializer

class TopicsViewSet(viewsets.ModelViewSet):
    queryset = Topics.objects.all().order_by('order_id')
    serializer_class = TopicsSerializer
