import asyncio
import base64
import json
import random

from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from rest_framework import viewsets

from topics.models import Topics
from topics.serializers import TopicsSerializer


class TopicsViewSet(viewsets.ModelViewSet):
    queryset = Topics.objects.all().order_by("order_id")
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
    return JsonResponse({"timestamp": encoded_str})


@csrf_exempt
@require_POST
def check_answer(request):
    data = json.loads(request.body)
    question_title = data.get("question_title")
    answer = str(data.get("answer"))

    try:
        question = Topics.objects.get(title=question_title)
        if question.answer == answer:
            # 答案正确，更新通过状态
            question.pass_status = True
            question.save()
            return JsonResponse({"correct": True})
        else:
            # 答案错误
            return JsonResponse({"correct": False})
    except Topics.DoesNotExist:
        return JsonResponse({"correct": False, "error": "题目不存在"})


@require_GET
async def delay(request, delay_time):
    try:
        # 将delay_time转换为整数
        delay_time = int(delay_time)
    except ValueError:
        return JsonResponse({"error": "Invalid delay time"}, status=400)
    # 异步延迟指定秒数
    await asyncio.sleep(delay_time)
    # 获取当前时间戳
    timestamp = now().timestamp()
    # 返回JSON响应
    return JsonResponse({"timestamp": timestamp})


@require_GET
def get_client_ip(request):
    # 获取请求的IP地址
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    print(x_forwarded_for, request.META.get("REMOTE_ADDR"))
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    # 返回JSON响应
    return JsonResponse({"ip": ip})


def ajax(request):
    return JsonResponse(
        {
            "title": "动态内容示例",
            "author": "蜘蛛小侠",
            "date": "2024-07-31",
            "content": "这是通过API接口获取的动态内容。该内容包括标题、作者、日期和主要内容，全部由服务器端提供。",
        },
        json_dumps_params={"ensure_ascii": False},
    )


# 翻页网页
def pagination1(request, pageNo):
    if pageNo == 100:
        pageNo = 666
    data = {"data": f"这是第{pageNo}页的内容。"}
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})


# 假设更多的商品数据，包含商品名称和价格
products = [
    {
        "name": "华为手机",
        "price": 4000,
        "brand": "华为",
        "category": "手机",
        "image": "https://example.com/image1.jpg",
        "rating": 4.5,
        "reviews": 1200,
        "stock": 100,
        "sales": 300,
        "description": "高性能智能手机，搭载最新麒麟芯片",
    },
    {
        "name": "苹果笔记本",
        "price": 8000,
        "brand": "苹果",
        "category": "电脑",
        "image": "https://example.com/image2.jpg",
        "rating": 4.7,
        "reviews": 800,
        "stock": 50,
        "sales": 200,
        "description": "轻薄便携，适合商务办公",
    },
    {
        "name": "小米电视",
        "price": 2000,
        "brand": "小米",
        "category": "电视",
        "image": "https://example.com/image3.jpg",
        "rating": 4.3,
        "reviews": 1500,
        "stock": 200,
        "sales": 600,
        "description": "智能高清大屏，支持4K",
    },
    {
        "name": "戴森吸尘器",
        "price": 2500,
        "brand": "戴森",
        "category": "家电",
        "image": "https://example.com/image4.jpg",
        "rating": 4.9,
        "reviews": 600,
        "stock": 30,
        "sales": 100,
        "description": "强力吸尘，适用于各种地面",
    },
    {
        "name": "索尼耳机",
        "price": 1500,
        "brand": "索尼",
        "category": "耳机",
        "image": "https://example.com/image5.jpg",
        "rating": 4.8,
        "reviews": 900,
        "stock": 150,
        "sales": 450,
        "description": "高品质音效，舒适佩戴",
    },
    {
        "name": "三星冰箱",
        "price": 5000,
        "brand": "三星",
        "category": "家电",
        "image": "https://example.com/image6.jpg",
        "rating": 4.6,
        "reviews": 700,
        "stock": 80,
        "sales": 250,
        "description": "节能环保，静音设计",
    },
    {
        "name": "微软Surface Pro 7",
        "price": 6500,
        "brand": "微软",
        "category": "电脑",
        "image": "https://example.com/image7.jpg",
        "rating": 4.4,
        "reviews": 300,
        "stock": 90,
        "sales": 120,
        "description": "二合一平板，支持触摸和笔操作",
    },
    {
        "name": "联想ThinkPad X1 Carbon",
        "price": 9000,
        "brand": "联想",
        "category": "电脑",
        "image": "https://example.com/image8.jpg",
        "rating": 4.6,
        "reviews": 1100,
        "stock": 40,
        "sales": 80,
        "description": "高端商务笔记本，轻薄坚固",
    },
    {
        "name": "佳能相机",
        "price": 3500,
        "brand": "佳能",
        "category": "相机",
        "image": "https://example.com/image9.jpg",
        "rating": 4.7,
        "reviews": 700,
        "stock": 100,
        "sales": 200,
        "description": "高像素数码单反相机，适合摄影爱好者",
    },
    {
        "name": "尼康相机",
        "price": 3000,
        "brand": "尼康",
        "category": "相机",
        "image": "https://example.com/image10.jpg",
        "rating": 4.5,
        "reviews": 500,
        "stock": 80,
        "sales": 150,
        "description": "便捷小巧的数码相机，适合日常拍摄",
    },
    {
        "name": "飞利浦空气净化器",
        "price": 2200,
        "brand": "飞利浦",
        "category": "家电",
        "image": "https://example.com/image11.jpg",
        "rating": 4.8,
        "reviews": 1500,
        "stock": 50,
        "sales": 400,
        "description": "高效空气净化，改善空气质量",
    },
    {
        "name": "Bose音响",
        "price": 3500,
        "brand": "Bose",
        "category": "音响",
        "image": "https://example.com/image12.jpg",
        "rating": 4.9,
        "reviews": 2000,
        "stock": 120,
        "sales": 500,
        "description": "无与伦比的音效，蓝牙连接",
    },
    {
        "name": "飞利浦电动牙刷",
        "price": 500,
        "brand": "飞利浦",
        "category": "个人护理",
        "image": "https://example.com/image13.jpg",
        "rating": 4.6,
        "reviews": 800,
        "stock": 100,
        "sales": 300,
        "description": "智能电动牙刷，有效清洁牙齿",
    },
    {
        "name": "德龙咖啡机",
        "price": 1800,
        "brand": "德龙",
        "category": "家电",
        "image": "https://example.com/image14.jpg",
        "rating": 4.7,
        "reviews": 900,
        "stock": 50,
        "sales": 150,
        "description": "高品质咖啡机，适合家庭使用",
    },
    {
        "name": "瑞士军刀",
        "price": 350,
        "brand": "瑞士军刀",
        "category": "户外",
        "image": "https://example.com/image15.jpg",
        "rating": 4.9,
        "reviews": 700,
        "stock": 100,
        "sales": 250,
        "description": "多功能便携工具，适合户外活动",
    },
    {
        "name": "耐克跑步鞋",
        "price": 900,
        "brand": "耐克",
        "category": "运动",
        "image": "https://example.com/image16.jpg",
        "rating": 4.5,
        "reviews": 1500,
        "stock": 80,
        "sales": 400,
        "description": "舒适运动鞋，适合跑步使用",
    },
    {
        "name": "阿迪达斯运动裤",
        "price": 600,
        "brand": "阿迪达斯",
        "category": "运动",
        "image": "https://example.com/image17.jpg",
        "rating": 4.3,
        "reviews": 1200,
        "stock": 150,
        "sales": 500,
        "description": "透气舒适的运动裤",
    },
    {
        "name": "松下剃须刀",
        "price": 700,
        "brand": "松下",
        "category": "个人护理",
        "image": "https://example.com/image18.jpg",
        "rating": 4.6,
        "reviews": 400,
        "stock": 200,
        "sales": 600,
        "description": "高效剃须，适合男士使用",
    },
    {
        "name": "飞利浦剃须刀",
        "price": 650,
        "brand": "飞利浦",
        "category": "个人护理",
        "image": "https://example.com/image19.jpg",
        "rating": 4.7,
        "reviews": 500,
        "stock": 100,
        "sales": 350,
        "description": "舒适剃须，减少皮肤刺激",
    },
    {
        "name": "小米智能手表",
        "price": 500,
        "brand": "小米",
        "category": "智能设备",
        "image": "https://example.com/image20.jpg",
        "rating": 4.4,
        "reviews": 800,
        "stock": 120,
        "sales": 400,
        "description": "健康监测，运动追踪",
    },
    {
        "name": "Apple Watch",
        "price": 2500,
        "brand": "苹果",
        "category": "智能设备",
        "image": "https://example.com/image21.jpg",
        "rating": 4.8,
        "reviews": 1500,
        "stock": 60,
        "sales": 250,
        "description": "精准健康监测，时尚外观",
    },
    {
        "name": "三星手机",
        "price": 3500,
        "brand": "三星",
        "category": "手机",
        "image": "https://example.com/image22.jpg",
        "rating": 4.6,
        "reviews": 1100,
        "stock": 200,
        "sales": 700,
        "description": "高清屏幕，快速充电",
    },
    {
        "name": "荣耀手机",
        "price": 2500,
        "brand": "荣耀",
        "category": "手机",
        "image": "https://example.com/image23.jpg",
        "rating": 4.3,
        "reviews": 700,
        "stock": 150,
        "sales": 400,
        "description": "性价比高，适合日常使用",
    },
    {
        "name": "美的空调",
        "price": 5000,
        "brand": "美的",
        "category": "家电",
        "image": "https://example.com/image24.jpg",
        "rating": 4.7,
        "reviews": 1200,
        "stock": 70,
        "sales": 300,
        "description": "节能空调，快速降温",
    },
    {
        "name": "奥克斯空调",
        "price": 3500,
        "brand": "奥克斯",
        "category": "家电",
        "image": "https://example.com/image25.jpg",
        "rating": 4.4,
        "reviews": 800,
        "stock": 150,
        "sales": 500,
        "description": "高效能空调，适合夏季使用",
    },
    {
        "name": "海尔冰箱",
        "price": 3000,
        "brand": "海尔",
        "category": "家电",
        "image": "https://example.com/image26.jpg",
        "rating": 4.5,
        "reviews": 1000,
        "stock": 120,
        "sales": 600,
        "description": "节能环保冰箱，持久保鲜",
    },
    {
        "name": "华硕显卡",
        "price": 4000,
        "brand": "华硕",
        "category": "电脑配件",
        "image": "https://example.com/image27.jpg",
        "rating": 4.6,
        "reviews": 500,
        "stock": 80,
        "sales": 300,
        "description": "强大性能，支持最新游戏",
    },
    {
        "name": "英伟达显卡",
        "price": 4500,
        "brand": "英伟达",
        "category": "电脑配件",
        "image": "https://example.com/image28.jpg",
        "rating": 4.7,
        "reviews": 1000,
        "stock": 100,
        "sales": 450,
        "description": "超高性能，适合游戏和专业设计",
    },
    {
        "name": "西部数据硬盘",
        "price": 800,
        "brand": "西部数据",
        "category": "电脑配件",
        "image": "https://example.com/image29.jpg",
        "rating": 4.3,
        "reviews": 600,
        "stock": 200,
        "sales": 500,
        "description": "高容量硬盘，快速读写",
    },
    {
        "name": "希捷硬盘",
        "price": 700,
        "brand": "希捷",
        "category": "电脑配件",
        "image": "https://example.com/image30.jpg",
        "rating": 4.5,
        "reviews": 500,
        "stock": 150,
        "sales": 400,
        "description": "高性能硬盘，适合大数据存储",
    },
    {
        "name": "JBL蓝牙音响",
        "price": 900,
        "brand": "JBL",
        "category": "音响",
        "image": "https://example.com/image31.jpg",
        "rating": 4.6,
        "reviews": 800,
        "stock": 100,
        "sales": 450,
        "description": "便携式蓝牙音响，音质优良",
    },
    {
        "name": "荣耀平板",
        "price": 1200,
        "brand": "荣耀",
        "category": "平板",
        "image": "https://example.com/image32.jpg",
        "rating": 4.4,
        "reviews": 300,
        "stock": 80,
        "sales": 200,
        "description": "高性价比平板，适合娱乐使用",
    },
    {
        "name": "iPad Pro",
        "price": 7000,
        "brand": "苹果",
        "category": "平板",
        "image": "https://example.com/image33.jpg",
        "rating": 4.9,
        "reviews": 1500,
        "stock": 50,
        "sales": 100,
        "description": "强大性能，适合创作和娱乐",
    },
    {
        "name": "华为平板",
        "price": 2500,
        "brand": "华为",
        "category": "平板",
        "image": "https://example.com/image34.jpg",
        "rating": 4.7,
        "reviews": 600,
        "stock": 100,
        "sales": 400,
        "description": "流畅体验，支持多种应用",
    },
    {
        "name": "小米平板",
        "price": 1500,
        "brand": "小米",
        "category": "平板",
        "image": "https://example.com/image35.jpg",
        "rating": 4.2,
        "reviews": 400,
        "stock": 120,
        "sales": 350,
        "description": "性价比高，适合学习和娱乐",
    },
    {
        "name": "三星平板",
        "price": 2500,
        "brand": "三星",
        "category": "平板",
        "image": "https://example.com/image36.jpg",
        "rating": 4.5,
        "reviews": 800,
        "stock": 150,
        "sales": 450,
        "description": "大屏幕，高清显示",
    },
    {
        "name": "酷派手机",
        "price": 1000,
        "brand": "酷派",
        "category": "手机",
        "image": "https://example.com/image37.jpg",
        "rating": 3.9,
        "reviews": 500,
        "stock": 200,
        "sales": 700,
        "description": "经济实用型手机",
    },
    {
        "name": "小米米家电器套装",
        "price": 3000,
        "brand": "小米",
        "category": "家电",
        "image": "https://example.com/image38.jpg",
        "rating": 4.5,
        "reviews": 600,
        "stock": 150,
        "sales": 500,
        "description": "一站式智能家居，提升生活品质",
    },
    {
        "name": "华为Mate 40",
        "price": 6500,
        "brand": "华为",
        "category": "手机",
        "image": "https://example.com/image39.jpg",
        "rating": 4.8,
        "reviews": 1200,
        "stock": 80,
        "sales": 350,
        "description": "超高清影像系统，强悍性能",
    },
    {
        "name": "三星Galaxy Z Fold",
        "price": 12000,
        "brand": "三星",
        "category": "手机",
        "image": "https://example.com/image40.jpg",
        "rating": 4.9,
        "reviews": 1500,
        "stock": 30,
        "sales": 100,
        "description": "折叠屏幕，革新体验",
    },
    {
        "name": "华硕ROG游戏本",
        "price": 13000,
        "brand": "华硕",
        "category": "电脑",
        "image": "https://example.com/image41.jpg",
        "rating": 4.8,
        "reviews": 900,
        "stock": 50,
        "sales": 200,
        "description": "专业游戏笔记本，强悍性能",
    },
    {
        "name": "雷蛇游戏鼠标",
        "price": 800,
        "brand": "雷蛇",
        "category": "外设",
        "image": "https://example.com/image42.jpg",
        "rating": 4.7,
        "reviews": 1000,
        "stock": 100,
        "sales": 500,
        "description": "精准控制，舒适握感",
    },
    {
        "name": "机械键盘",
        "price": 1200,
        "brand": "Corsair",
        "category": "外设",
        "image": "https://example.com/image43.jpg",
        "rating": 4.5,
        "reviews": 700,
        "stock": 80,
        "sales": 300,
        "description": "高效键盘，适合游戏和编程",
    },
    {
        "name": "苹果耳机",
        "price": 1000,
        "brand": "苹果",
        "category": "耳机",
        "image": "https://example.com/image44.jpg",
        "rating": 4.8,
        "reviews": 1500,
        "stock": 100,
        "sales": 450,
        "description": "高品质音效，舒适佩戴",
    },
    {
        "name": "华为耳机",
        "price": 600,
        "brand": "华为",
        "category": "耳机",
        "image": "https://example.com/image45.jpg",
        "rating": 4.5,
        "reviews": 400,
        "stock": 200,
        "sales": 600,
        "description": "降噪耳机，适合长时间佩戴",
    },
    {
        "name": "小米米家扫地机器人",
        "price": 1500,
        "brand": "小米",
        "category": "家电",
        "image": "https://example.com/image46.jpg",
        "rating": 4.7,
        "reviews": 1000,
        "stock": 50,
        "sales": 300,
        "description": "智能扫地，解放双手",
    },
    {
        "name": "博世洗碗机",
        "price": 4500,
        "brand": "博世",
        "category": "家电",
        "image": "https://example.com/image47.jpg",
        "rating": 4.8,
        "reviews": 500,
        "stock": 80,
        "sales": 250,
        "description": "高效节能洗碗机，省时省力",
    },
    {
        "name": "小米空气净化器",
        "price": 1200,
        "brand": "小米",
        "category": "家电",
        "image": "https://example.com/image48.jpg",
        "rating": 4.6,
        "reviews": 600,
        "stock": 100,
        "sales": 450,
        "description": "高效空气净化，适合家庭使用",
    },
]


def pagination_table(request, page):
    items_per_page = 10  # 每页显示20个商品
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    # 随机选择每页的商品数据
    random.shuffle(products)  # 打乱商品列表顺序
    data = products[start_index:end_index]  # 取当前页的数据

    # 返回JSON响应
    return JsonResponse({"data": data})


@csrf_exempt
def post_intro_json(request):
    if request.method == "POST":
        data = json.loads(request.body)  # 解析请求体中的 JSON 数据
        password = data.get('password', None)

        if password != 'post':
            return JsonResponse({'error': '密码不正确'}, status=403)

        intro_content = {
            "title": "POST 请求介绍",
            "content": """
                POST 请求是 HTTP 协议中常用的一种请求方法，通常用于向服务器提交数据。
                与 GET 请求不同，POST 请求的参数不会附加在 URL 中，而是放在请求体（Body）中。
                POST 请求用于表单提交、用户登录、注册、文件上传等场景。它的特点包括：
                <ul>
                    <li>请求参数通过请求体（Body）传递，而不是附加在 URL 后。</li>
                    <li>没有长度限制，可以传输大量数据。</li>
                    <li>会修改服务器的数据或创建新的资源。</li>
                    <li>通常不是幂等的，每次请求可能会产生不同的结果。</li>
                </ul>
            """
        }
        return JsonResponse(intro_content)
    else:
        return JsonResponse({'error': '只支持 POST 请求'}, status=400)


@csrf_exempt
def post_intro_form(request):
    if request.method == "POST":
        password = request.POST.get('password', None)
        if password != 'post':
            return JsonResponse({'error': '密码不正确'}, status=403)
        intro_content = {
            "title": "POST 请求类型：JSON 与表单的区别",
            "content": """
                <h3>1. 表单格式 (application/x-www-form-urlencoded)</h3>
                <p>
                    表单格式是最常见的 POST 请求格式。在这种格式下，数据通过键值对传递，数据被编码为 `key=value` 的形式，
                    适合简单的数据提交，如用户名、密码等。表单数据会经过 URL 编码，格式类似 `key1=value1&key2=value2`，通常用于传统表单。
                </p>
                <h3>示例：</h3>
                <pre>
                POST /submit_form HTTP/1.1
                Host: example.com
                Content-Type: application/x-www-form-urlencoded
                Content-Length: 43

                username=alice&password=12345&email=alice%40mail.com
                </pre>

                <h3>2. JSON 格式 (application/json)</h3>
                <p>
                    JSON 格式适合提交结构化的数据，尤其是在 API 交互中。JSON 格式可以支持更复杂的嵌套数据，
                    比如对象和数组，通常用于与 RESTful API 进行交互。JSON 格式的数据通常通过 `application/json` 类型提交。
                </p>
                <h3>示例：</h3>
                <pre>
                POST /submit_data HTTP/1.1
                Host: example.com
                Content-Type: application/json
                Content-Length: 55

                {
                    "username": "alice",
                    "password": "12345",
                    "email": "alice@mail.com"
                }
                </pre>
                <h3>总结：</h3>
                <ul>
                    <li><b>表单格式：</b>适用于简单的数据提交，通常用于传统的表单提交。</li>
                    <li><b>JSON 格式：</b>适用于复杂的、结构化的数据提交，常用于与 API 的交互。</li>
                </ul>
            """
        }
        return JsonResponse(intro_content)
    else:
        return JsonResponse({'error': '只支持 POST的表单 请求'}, status=400)


@require_GET
def base64_encode(request):
    input_string = request.GET.get("string", "")
    print(input_string)
    encoded_string = base64.b64encode(input_string.encode()).decode()
    return JsonResponse({"encoded_string": encoded_string})


@require_GET
def base64_decode(request):
    input_string = request.GET.get("string", "")
    try:
        decoded_string = base64.b64decode(input_string).decode()
    except Exception as e:
        return JsonResponse({"error": "Invalid Base64 string"}, status=400)
    return JsonResponse({"decoded_string": decoded_string})


@require_GET
def reverse_string(request):
    input_string = request.GET.get("string", "")
    reversed_string = input_string[::-1]
    return JsonResponse({"reversed_string": reversed_string})


@require_GET
def get_request_headers(request):
    headers = {
        key: value for key, value in request.META.items() if key.startswith("HTTP_")
    }
    return JsonResponse({"headers": headers})


@require_GET
def health_check(request):
    return JsonResponse({"status": "ok"})


@require_GET
def get_user_agent(request):
    user_agent = request.META.get("HTTP_USER_AGENT", "unknown")
    return JsonResponse({"user_agent": user_agent})


@require_GET
def get_server_time(request):
    current_time = now().timestamp()
    return JsonResponse({"server_time": current_time})
