import asyncio
import base64
import json

from django.http import JsonResponse
from django.utils import timezone
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from rest_framework import viewsets

from topics.models import Topics
from topics.serializers import TopicsSerializer


class TopicsViewSet(viewsets.ModelViewSet):
    queryset = Topics.objects.all().order_by('order_id')
    serializer_class = TopicsSerializer

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

@csrf_exempt
@require_POST
def check_answer(request):
    data = json.loads(request.body)
    question_title = data.get('question_title')
    answer = str(data.get('answer'))

    try:
        question = Topics.objects.get(title=question_title)
        if question.answer == answer:
            # 答案正确，更新通过状态
            question.pass_status = True
            question.save()
            return JsonResponse({'correct': True})
        else:
            # 答案错误
            return JsonResponse({'correct': False})
    except Topics.DoesNotExist:
        return JsonResponse({'correct': False, 'error': '题目不存在'})

@require_GET
async def delay(request, delay_time):
    try:
        # 将delay_time转换为整数
        delay_time = int(delay_time)
    except ValueError:
        return JsonResponse({'error': 'Invalid delay time'}, status=400)
    # 异步延迟指定秒数
    await asyncio.sleep(delay_time)
    # 获取当前时间戳
    timestamp = now().timestamp()
    # 返回JSON响应
    return JsonResponse({'timestamp': timestamp})

@require_GET
def get_client_ip(request):
    # 获取请求的IP地址
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(x_forwarded_for,request.META.get('REMOTE_ADDR'))
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # 返回JSON响应
    return JsonResponse({'ip': ip})
from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import base64
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def base64_encode(request):
    input_string = request.GET.get('string', '')
    print(input_string)
    encoded_string = base64.b64encode(input_string.encode()).decode()
    return JsonResponse({'encoded_string': encoded_string})

@require_GET
def base64_decode(request):
    input_string = request.GET.get('string', '')
    try:
        decoded_string = base64.b64decode(input_string).decode()
    except Exception as e:
        return JsonResponse({'error': 'Invalid Base64 string'}, status=400)
    return JsonResponse({'decoded_string': decoded_string})

@require_GET
def reverse_string(request):
    input_string = request.GET.get('string', '')
    reversed_string = input_string[::-1]
    return JsonResponse({'reversed_string': reversed_string})

@require_GET
def get_request_headers(request):
    headers = {key: value for key, value in request.META.items() if key.startswith('HTTP_')}
    return JsonResponse({'headers': headers})

@require_GET
def health_check(request):
    return JsonResponse({'status': 'ok'})

@require_GET
def get_user_agent(request):
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    return JsonResponse({'user_agent': user_agent})

@require_GET
def get_server_time(request):
    current_time = now().timestamp()
    return JsonResponse({'server_time': current_time})
