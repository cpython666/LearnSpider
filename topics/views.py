from django.shortcuts import get_object_or_404

from .models import Topics
from .decorators import require_ua
import time
import random
from django.shortcuts import render

def demo(request):
    return render(request, 'topics/pages/demo_get_server_time.html')

def demo1(request):
    return render(request, 'topics/pages/demo.html')
def hello_spider(request):#random_greetings
    greetings = []
    button_classes = [
        "btn btn-primary",
        "btn btn-secondary",
        "btn btn-success",
        "btn btn-danger",
        "btn btn-warning",
        "btn btn-info",
        "btn btn-light",
        "btn btn-dark",
        "btn btn-link"
    ]
    # 随机生成 666 个 "Hello, Spider~"
    for _ in range(666):
        greetings.append("Hello, Spider~")
    # 随机生成 "你好～世界！" 的数量（例如，随机 1 到 100 个）
    nihao_count = random.randint(1, 100)
    for _ in range(nihao_count):
        greetings.append("你好～世界！")
    # 随机生成 "Hello, World～" 的数量（例如，随机 1 到 100 个）
    hello_world_count = random.randint(1, 100)
    for _ in range(hello_world_count):
        greetings.append("Hello, World～")
    # 为每个 greeting 随机选择一个按钮样式
    greeting_buttons = [(greeting, random.choice(button_classes)) for greeting in greetings]
    # 打乱顺序
    random.shuffle(greeting_buttons)

    return render(request, 'topics/views/hello-spider.html', {'greeting_buttons': greeting_buttons})

def ua(request):
    return render(request, 'topics/views/ua.html')
def encode_page(request):
    response = render(request, 'topics/views/encode.html')
    response['Content-Type'] = 'text/html;'
    # response['Content-Type'] = 'text/html; charset=GB2312'
    # response['Content-Type'] = 'text/html;UTF-8'
    # response['Content-Type'] = 'text/html; charset=ISO-8859-1'
    return response

def request_twice(request):
    # get_content_or_script
    # 设定 Cookie 的过期时间为一秒
    # 考虑到以下几点，仍然进行过期时间的判断是一个更健壮的设计：
    # 浏览器行为不一致: 不同浏览器可能在处理过期Cookie时有不同的行为，有些可能不会立即删除。
    # 用户行为不确定: 用户可能会手动修改浏览器时间，或者在极端情况下，浏览器可能不会及时删除过期的Cookie。
    # 潜在的安全问题: 不信任客户端数据的完整性始终是一个好的安全实践。
    # 因此，尽管浏览器应该删除过期的Cookie，后端进行过期时间的验证仍然是推荐的做法，以确保系统的可靠性和安全性。
    COOKIE_NAME = 'timestamp'
    COOKIE_EXPIRATION = 1  # 秒
    # 读取 Cookie
    cookie_value = request.COOKIES.get(COOKIE_NAME)
    if cookie_value:
        try:
            # 验证 Cookie 是否过期
            cookie_timestamp = float(cookie_value)
            current_time = time.time()
            if current_time - cookie_timestamp <= COOKIE_EXPIRATION:
                # 如果 Cookie 仍然有效，返回 HTML 内容
                return render(request, 'topics/views/request-twice.html')
        except ValueError:
            pass
    # 如果没有有效的 Cookie，返回 JavaScript 代码来设置 Cookie
    return render(request, 'topics/views/request-twice-cookie.html')


def index(request):
    return render(request, 'topics/index.html')

def list(request):
    return render(request, 'topics/list.html')
def tools(request):
    return render(request, 'topics/tools.html')
def shorthand(request):
    return render(request, 'topics/shorthand.html')
def solutions(request):
    return render(request, 'topics/solutions.html')



def topic_view(request, response_path):
    # 根据 path 获取对应的题目
    topic = get_object_or_404(Topics, response_path=response_path)
    # 返回对应的 HTML 视图
    return render(request, 'topics/pages/'+response_path+'.html', {'topic': topic})

def error404(request, exception):
    return render(request, 'topics/404.html', status=404)
