from typing import Iterable

import scrapy
from scrapy import Request


class UseDpSpiderSpider(scrapy.Spider):
    name = "use_dp_spider"
    # start_urls = ["http://localhost:8001/"]
    start_urls = ["http://localhost:8001/","http://localhost:8001/","http://localhost:8001/","http://localhost:8001/"]
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "demo.drissionpage_middlewares.DrissionPageDownloaderMiddleware": 545,
        },
    }

    def start_requests(self) -> Iterable[Request]:
        for url in self.start_urls:
            yield Request(url, callback=self.parse,dont_filter=True,meta={"use_dp":True})
    def parse(self, response):
        print(response.xpath("//title/text()").get())
