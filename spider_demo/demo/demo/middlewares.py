from scrapy import signals
import random
from typing import Optional, Dict, Any


from twisted.internet.threads import deferToThread
from scrapy.http import HtmlResponse, Headers


class ProxyDownloaderMiddleware:
    """
    使用代理的下载器中间件（仅使用统一 PROXY_URL）：
    - 从 settings 读取 PROXY_URL
    - 为请求设置 request.meta['proxy']
    - 可通过 request.meta['no_proxy']=True 跳过某些请求
    """

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        settings = crawler.settings
        s.proxy_url = settings.get("PROXY_URL")
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # 若设置了 no_proxy 或未配置 PROXY_URL，跳过

        if request.meta.get("no_proxy") or not self.proxy_url:
            return None

        # 如果请求已经携带了代理，沿用它
        current = request.meta.get("proxy")
        if current:
            spider.logger.info(f"沿用请求自带代理: {current} -> {request.url}")
            return None

        # 仅使用统一的 PROXY_URL
        proxy = self.proxy_url

        if proxy:
            request.meta["proxy"] = proxy
            spider.logger.info(f"使用代理 {proxy} 请求 {request.url}")
        else:
            spider.logger.debug(f"未配置代理，直连: {request.url}")
        return None

    def process_exception(self, request, exception, spider):
        # 记录代理阶段的异常，交由后续中间件/默认处理
        spider.logger.warning(f"下载异常，url={request.url}, error={exception}")
        return None

    def spider_opened(self, spider):
        spider.logger.info(
            f"ProxyDownloaderMiddleware 已加载, PROXY_URL={getattr(self,'proxy_url',None)}"
        )


class RequestHeadersMiddleware:
    """
    请求头中间件：
    - 从 settings 读取 REQUEST_HEADERS（dict）
    - 可通过 request.meta['no_headers_mw']=True 跳过
    """

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        settings = crawler.settings
        s.headers = settings.get("REQUEST_HEADERS") or {}
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        if request.meta.get("no_headers_mw"):
            return None
        if request.meta.get("headers_none"):
            request.headers = Headers()
            return None
        request.headers = self.headers
        return None

    def spider_opened(self, spider):
        spider.logger.info(
            f"RequestHeadersMiddleware 已加载, defaults={list(getattr(self,'headers',{}).keys())}"
        )


class CurlCffiTLSDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        s.default_impersonate = crawler.settings.get("TLS_IMPERSONATE", "chrome")
        return s

    def process_request(self, request, spider):
        if not request.meta.get("use_curl_cffi"):
            return None
        from curl_cffi import requests as curl_requests

        def _do_request():
            url = request.url
            method = request.method.upper()
            impersonate = request.meta.get("impersonate", getattr(self, "default_impersonate", "chrome"))
            proxy = request.meta.get("proxy")
            proxies = {"http": proxy, "https": proxy} if proxy else None

            kwargs: Dict[str, Any] = {"headers": request.headers, "impersonate": impersonate}
            if proxies:
                kwargs["proxies"] = proxies

            if method in ("GET", "HEAD"):
                resp = curl_requests.request(method, url, **kwargs)
            else:
                body = request.body or None
                resp = curl_requests.request(method, url, data=body, **kwargs)

            body_bytes = resp.content or b""

            return HtmlResponse(
                url=resp.url or url,
                status=resp.status_code,
                body=body_bytes,
                request=request,
                encoding=resp.encoding or "utf-8",
            )

        return deferToThread(_do_request)