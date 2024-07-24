from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Topics

from LearnSpider.settings import topics_path_prefix
def demo(request):
    return render(request, 'topics/list/demo_get_server_time.html')


from django.http import HttpResponse, JsonResponse
from django.utils import timezone
import time


def request_twice(request):
    # get_content_or_script
    # 设定 Cookie 的过期时间为一秒
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
                return HttpResponse('<html><body><h1>Welcome to the page!</h1></body></html>')
        except ValueError:
            pass

    # 如果没有有效的 Cookie，返回 JavaScript 代码来设置 Cookie
    response_content = """
    <html>
    <body>
        <script type="text/javascript">
            // 设置 Cookie
            var cookieName = 'timestamp';
            var cookieValue = new Date().getTime() / 1000; // 当前时间戳（秒）
            var cookieExpiration = new Date(new Date().getTime() + 1000); // 过期时间为一秒后
            document.cookie = cookieName + '=' + cookieValue + '; expires=' + cookieExpiration.toUTCString() + '; path=/';
            // 重新加载页面
            window.location.reload();
        </script>
    </body>
    </html>
    """

    return HttpResponse(response_content, content_type='text/html')


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
    return render(request, 'topics/list/'+response_path+'.html', {'topic': topic})

def error404(request, exception):
    return render(request, 'topics/404.html', status=404)
