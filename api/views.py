# 在 api 应用的 views.py 文件中定义视图类

from rest_framework import viewsets
from topics.models import Topics
from topics.serializers import TopicsSerializer

class TopicsViewSet(viewsets.ModelViewSet):
    queryset = Topics.objects.all().order_by('order_id')
    serializer_class = TopicsSerializer


import time
import base64
from django.http import JsonResponse
from django.utils import timezone


def get_server_timestamp(request):
    # 生成当前13位时间戳
    server_time = int(timezone.now().timestamp() * 1000)
    # 计算每一位数字的和
    digit_sum = sum(int(digit) for digit in str(server_time))
    # 拼接和数值在时间戳前面
    combined_str = f"{digit_sum}{server_time}"
    # 使用 Base64 编码
    encoded_str = base64.b64encode(combined_str.encode()).decode()
    return JsonResponse({'timestamp': encoded_str})
