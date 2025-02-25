from typing import Iterable

import scrapy
from scrapy import Request


class HelloScrapySpider(scrapy.Spider):
    name = "hello_scrapy"
    # allowed_domains = ["baidu.com"]
    start_urls = ["https://cn.bing.com/"]

    def start_requests(self) -> Iterable[Request]:
        yield Request("http://localhost:8001/", callback=self.parse)

    def parse(self, response):
        print(1, response)
        print(response.css('.h1::text').get())
        urls = ['http://localhost:8001/?sort=asc&param=1', 'http://localhost:8001/?param=1&sort=asc']
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_local, meta={'aaa': 111}, dont_filter=True)

    def parse_local(self, response):
        print('请求了一次')
        # print(response.meta.get('aaa'))
        # print(response)
