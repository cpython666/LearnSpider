BOT_NAME = "demo"

SPIDER_MODULES = ["demo.spiders"]
NEWSPIDER_MODULE = "demo.spiders"

ROBOTSTXT_OBEY = False

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

PROXY_URL = "http://127.0.0.1:7890"

# 配置请求头与 UA（仅对本爬虫生效）
REQUEST_HEADERS_OVERWRITE = True
REQUEST_HEADERS = {
    "Accept-Language": "zh-CN,zh;q=0.9"
}

REQUEST_USER_AGENT_LIST = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
]
