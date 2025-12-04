from twisted.internet.threads import deferToThread
from scrapy.http import HtmlResponse
from DrissionPage import Chromium

class DrissionPageDownloaderMiddleware:
    def __init__(self):
        self.chrome=Chromium()

    def process_request(self, request, spider):
        if not request.meta.get("use_dp"):
            return None

        def _do_request():
            url = request.url
            new_tab = self.chrome.new_tab()
            new_tab.get(url)
            url=new_tab.url
            body=new_tab.html
            new_tab.close()

            return HtmlResponse(
                url=url,
                body=body,
                request=request,
                encoding="utf-8",
            )

        return deferToThread(_do_request)