import scrapy


class WalmartTLSSpider(scrapy.Spider):
    name = "walmart_tls"
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "demo.middlewares.RequestHeadersMiddleware": 542,
            # "demo.middlewares.ProxyDownloaderMiddleware": 543,
            "demo.middlewares.CurlCffiTLSDownloaderMiddleware": 545,
        },
    }

    def start_requests(self):
        url = "https://www.walmart.com/search?q=keyboard"
        yield scrapy.Request(
            url,
            meta={
                "use_curl_cffi": True,
                "impersonate": "chrome",
                "headers_none": True,
            },
        )

    def parse(self, response):
        print(response)
        print(response.text)