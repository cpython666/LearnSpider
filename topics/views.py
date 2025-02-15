from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Topics
from .decorators import require_ua
import time
import random
from django.shortcuts import render


def demo(request):
    return render(request, 'topics/pages/demo_get_server_time.html')


def demo1(request):
    return render(request, 'topics/pages/demo.html')


def hello_spider(request):  # random_greetings
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


@require_ua
def ua(request):
    return render(request, 'topics/views/ua.html')


def encode_page(request):
    response = render(request, 'topics/views/encode.html')
    response['Content-Type'] = 'text/html;'
    # response['Content-Type'] = 'text/html; charset=GB2312'
    # response['Content-Type'] = 'text/html;UTF-8'
    # response['Content-Type'] = 'text/html; charset=ISO-8859-1'
    return response


def table(request):
    # 定义行数和列数，这里可以随机生成，或者根据你的需求来确定
    rows = random.randint(5, 10)
    cols = random.randint(5, 10)

    # 生成随机的表格数据，确保总和为666666
    total_sum = 666666
    table_data = [[0] * cols for _ in range(rows)]
    remaining_sum = total_sum

    for r in range(rows):
        for c in range(cols):
            if r == rows - 1 and c == cols - 1:
                table_data[r][c] = remaining_sum  # 最后一个单元格填充剩余的数值
            else:
                # 确保 max_value 始终大于等于 1
                max_value = max(1, remaining_sum - (rows - r - 1) * (cols - c - 1))
                value = random.randint(1, max_value)
                table_data[r][c] = value
                remaining_sum -= value

    context = {
        'table_data': table_data
    }
    return render(request, 'topics/views/table.html', context)


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
    return render(request, 'topics/index/index.html')


def list(request):
    return render(request, 'topics/index/list.html')


def tools(request):
    return render(request, 'topics/index/tools.html')


def sandbox(request):
    return render(request, 'topics/index/sandbox.html')


def sandbox_news(request):
    # 模拟一些假新闻数据
    latest_news = [
        {
            'id': 1,
            'title': '新科技革命：AI 将重塑未来',
            'summary': '随着 AI 技术的飞速发展，未来的科技将发生翻天覆地的变化...',
            'publish_date': datetime.now().strftime('%Y-%m-%d'),
        },
        {
            'id': 2,
            'title': '2025年全球互联网将迎来新变革',
            'summary': '在未来几年，全球互联网将经历一场前所未有的革命...',
            'publish_date': datetime.now().strftime('%Y-%m-%d'),
        },
        {
            'id': 3,
            'title': '量子计算的突破性进展',
            'summary': '量子计算作为一种新型计算模式，正在逐步突破技术瓶颈...',
            'publish_date': datetime.now().strftime('%Y-%m-%d'),
        },
        {
            'id': 4,
            'title': '5G网络加速全球数字化进程',
            'summary': '5G网络的普及正在改变全球通信格局，推动各行各业的数字化转型...',
            'publish_date': datetime.now().strftime('%Y-%m-%d'),
        },
        {
            'id': 5,
            'title': '未来科技：机器人将进入家庭生活',
            'summary': '随着人工智能和机器人技术的发展，智能机器人正在进入普通家庭...',
            'publish_date': datetime.now().strftime('%Y-%m-%d'),
        },
    ]

    return render(request, 'topics/sandbox/news/news_index.html',
                  {'latest_news': latest_news, "search": '/sandbox/news/search'})


# 模拟分类和新闻数据
categories = [
    {
        'id': 1,
        'char_name': 'technology',
        'name': '科技',
        'news': [
            {'id': 1, 'title': 'AI 的未来', 'summary': '探索人工智能的最新发展...', 'publish_date': '2025-02-13'},
            {'id': 2, 'title': '5G 网络的全球影响', 'summary': '5G 网络带来的技术革新...',
             'publish_date': '2025-02-12'},
        ]
    },
    {
        'id': 2,
        'char_name': 'happy',
        'name': '娱乐',
        'news': [
            {'id': 3, 'title': '明星动态：新电影发布', 'summary': '最新电影上映，明星动态...',
             'publish_date': '2025-02-14'},
            {'id': 4, 'title': '2025年超级碗回顾', 'summary': '今年超级碗的精彩瞬间...',
             'publish_date': '2025-02-10'},
        ]
    },
    {
        'id': 3,
        'char_name': 'sport',
        'name': '体育',
        'news': [
            {'id': 5, 'title': '足球世界杯的传奇时刻', 'summary': '回顾世界杯历史上的经典时刻...',
             'publish_date': '2025-02-11'},
            {'id': 6, 'title': 'NBA 历史最佳球员排名', 'summary': 'NBA 球员排名持续更新...',
             'publish_date': '2025-02-09'},
        ]
    },
    {
        'id': 4,
        'char_name': 'web3',
        'name': 'Web3',
        'news': [
            {'id': 7, 'title': 'Web3：去中心化互联网的崛起',
             'summary': 'Web3 作为去中心化的互联网理念，正在改变许多行业...', 'publish_date': '2025-02-15'},
            {'id': 8, 'title': 'NFT 的未来：如何定义数字所有权',
             'summary': 'NFT 已成为区块链中的一个重要领域，它带来了数字资产的革命...', 'publish_date': '2025-02-14'},
            {'id': 9, 'title': 'DeFi：去中心化金融的现状与未来',
             'summary': 'DeFi 带来了无银行的金融模式，它能否挑战传统金融体系？', 'publish_date': '2025-02-13'},
        ]
    },
]


def sandbox_news_category(request):
    # 模拟数据：新闻来源平台和新闻类别
    sources = [
        {'name': '抖音', 'slug': 'douyin'},
        {'name': 'B站', 'slug': 'bilibili'},
        {'name': '知乎', 'slug': 'zhihu'},
    ]
    # 模拟数据：新闻类别
    categories = [
        {'name': '国际新闻', 'slug': 'international'},
        {'name': '国内新闻', 'slug': 'domestic'},
        {'name': '科技新闻', 'slug': 'technology'},
        {'name': '体育新闻', 'slug': 'sports'},
        {'name': '娱乐新闻', 'slug': 'entertainment'},
    ]

    # 将数据传递到模板
    return render(request, 'topics/sandbox/news/category.html', {'sources': sources, 'categories': categories})


def sandbox_news_category_detail(request, slug):
    # 模拟数据：新闻类别详情
    categories_details = {
        'international': {'name': '国际新闻', 'description': '全球范围内的新闻热点，聚焦国际局势。'},
        'domestic': {'name': '国内新闻', 'description': '关注本国的时事新闻，涵盖社会、政治、经济等各个方面。'},
        'technology': {'name': '科技新闻', 'description': '报道最新的科技趋势、创新产品和技术突破。'},
        'sports': {'name': '体育新闻', 'description': '关注体育赛事、运动员动态及全球体育新闻。'},
        'entertainment': {'name': '娱乐新闻', 'description': '报道娱乐圈的最新动态、明星资讯、影视作品等。'},
    }

    category = categories_details.get(slug, {})
    return render(request, 'topics/sandbox/news/detail_category.html', {'category': category})


def sandbox_news_source_detail(request, slug):
    # 模拟数据：来源平台详情
    sources_details = {
        'douyin': {'name': '抖音', 'description': '抖音是一款短视频分享社交平台，用户可以发布和观看短视频。'},
        'bilibili': {'name': 'B站', 'description': 'B站是一家以二次元文化为主的在线视频平台，提供丰富的视频内容。'},
        'zhihu': {'name': '知乎', 'description': '知乎是一个知识分享和问答社区，汇集了大量专业内容和用户互动。'},
    }

    source = sources_details.get(slug, {})
    print(source)
    return render(request, 'topics/sandbox/news/detail_source.html', {'source': source})


def sandbox_news_detail(request, id):
    # 假设根据id获取新闻，实际上只是返回假数据
    news_item = {
        'id': id,
        'title': f'新闻 {id} 详情',
        'content': '这是新闻的详细内容，更多的细节信息可以在这里展示。',
    }
    return render(request, 'topics/sandbox/news/detail_news.html',
                  {'news_item': news_item})


def sandbox_news_about_us(request):
    return render(request, 'topics/sandbox/news/about_us.html')


def sandbox_news_notice(request):
    return render(request, 'topics/sandbox/news/notice.html')


def shorthand(request):
    return render(request, 'topics/index/shorthand.html')


def solutions(request):
    return render(request, 'topics/solutions.html')


def topic_view(request, response_path):
    # 根据 path 获取对应的题目
    topic = get_object_or_404(Topics, response_path=response_path)
    # 返回对应的 HTML 视图
    return render(request, 'topics/pages/' + response_path + '.html', {'topic': topic})


def error404(request, exception):
    return render(request, 'topics/404.html', status=404)
