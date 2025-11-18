import json
import scrapy
from pprint import pprint

class ProxyTestSpider(scrapy.Spider):
    name = "proxy_test"
    custom_settings = {
        # 仅在本爬虫启用代理中间件；代理读取自 settings.PROXY_URL
        "DOWNLOADER_MIDDLEWARES": {
            "demo.middlewares.ProxyDownloaderMiddleware": 543,
            # 启用请求头中间件（先于代理执行）
            "demo.middlewares.RequestHeadersMiddleware": 542,
        },
    }
    start_urls = ["https://httpbin.org/get"]

    def parse(self, response):
        # 尝试解析 JSON 响应
        data = response.json()
        origin = data.get("origin")
        headers = data.get("headers", {})
        proxy_used = response.request.meta.get("proxy")

        self.logger.info(
            f"当前出口IP: {origin} | UA: {headers.get('User-Agent')} | 代理: {proxy_used}"
        )


        pprint(
            {
                "url": response.url,
                "origin": origin,
                "user_agent": headers.get("User-Agent"),
                "proxy": proxy_used,
            }
        )
