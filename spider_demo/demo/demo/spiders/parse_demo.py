import scrapy
from demo.items import NewsItem


class ParseDemoSpider(scrapy.Spider):
    custom_settings = {
        # "ITEM_PIPELINES": {
        #     'demo.pipelines.NewsPipeline': 1,  # 启用 NewsPipeline
        # },
        # "DOWNLOADER_MIDDLEWARES": {
        #     'demo.middlewares.DemoDownloaderMiddleware': 543
        # }
    }

    name = "parse_demo"
    start_urls = ["http://localhost:8001/sandbox/news/hot/"]

    def parse(self, response):
        card_lst = response.css('.card-body')
        for card in card_lst:
            # item = NewsItem()
            # item['title'] = card.css('a span::text').get()
            # item['url'] = card.css('a::attr(href)').get()
            yield {
                "title": card.css('a span::text').get(), "url": card.css('a::attr(href)').get()
            }
            # print(card.css('a span::text').get(), card.css('a::attr(href)').get())
            # yield item


if __name__ == '__main__':
    from scrapy import Selector

    text = '<a>111</a>'
    response = Selector(text=text)
    print(response.xpath('//a/text()').get())
