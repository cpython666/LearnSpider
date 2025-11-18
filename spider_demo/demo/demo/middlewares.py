from scrapy import signals
import random


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
    - 从 settings 读取 REQUEST_HEADERS（dict）、REQUEST_HEADERS_OVERWRITE（bool）、
      REQUEST_USER_AGENT（str）或 REQUEST_USER_AGENT_LIST（list）
    - 可通过 request.meta['no_headers_mw']=True 跳过
    """

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        settings = crawler.settings
        s.headers = settings.get("REQUEST_HEADERS") or {}
        s.overwrite = settings.getbool("REQUEST_HEADERS_OVERWRITE", True)
        s.user_agent = settings.get("REQUEST_USER_AGENT")
        s.user_agent_list = settings.get("REQUEST_USER_AGENT_LIST") or []
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # 跳过条件
        if request.meta.get("no_headers_mw"):
            return None

        # 设置 User-Agent
        ua = self.user_agent
        if not ua and self.user_agent_list:
            ua = random.choice(self.user_agent_list)
        if ua:
            if self.overwrite or b"User-Agent" not in request.headers:
                request.headers["User-Agent"] = ua

        # 合并设置的 headers
        for k, v in self.headers.items():
            key_bytes = k.encode() if isinstance(k, str) else k
            if self.overwrite or key_bytes not in request.headers:
                request.headers[k] = v

        return None

    def spider_opened(self, spider):
        spider.logger.info(
            f"RequestHeadersMiddleware 已加载, overwrite={getattr(self,'overwrite',None)}, "
            f"UA={'list' if getattr(self,'user_agent_list',[]) else getattr(self,'user_agent',None)}"
        )