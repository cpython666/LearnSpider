import scrapy
import json


class JsonRequestSpider(scrapy.Spider):
    name = "json_spider"

    start_urls = ["http://localhost:8001/api/post_intro_json/"]

    def start_requests(self):
        # JSON 数据
        data = {
            "password": "post",
        }

        # 请求头，指定发送 JSON 数据
        headers = {
            "Content-Type": "application/json",
        }

        # 发送 POST 请求
        yield scrapy.Request(
            url=self.start_urls[0],
            method="POST",
            headers=headers,
            body=json.dumps(data),  # 将字典转换为 JSON 字符串
            callback=self.parse,
        )

    def parse(self, response):
        # 解析响应数据
        data = json.loads(response.text)
        self.log(f"响应数据: {data}")


class FormRequestSpider(scrapy.Spider):
    name = "form_spider"

    start_urls = ["http://localhost:8001/api/post_intro_form/"]

    def start_requests(self):
        # JSON 数据
        formdata = {
            "password": "post",
        }

        # 发送 POST 请求
        yield scrapy.FormRequest(
            url=self.start_urls[0],
            method="POST",
            formdata=formdata,  # 将字典转换为 JSON 字符串
            callback=self.parse,
        )

    def parse(self, response):
        # 解析响应数据
        data = json.loads(response.text)
        self.log(f"响应数据: {data}")
