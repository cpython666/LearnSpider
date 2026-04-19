from scrapling.fetchers import StealthyFetcher, StealthySession

# 或使用一次性请求样式，为此请求打开浏览器，完成后关闭
# response = StealthyFetcher.fetch('https://nopecha.com/demo/cloudflare',solve_cloudflare=True)
# response = StealthyFetcher.fetch('https://academic.oup.com/adaptation/article/19/2/apag007/8551555',solve_cloudflare=True)
response = StealthyFetcher.fetch('https://oatd.org/oatd/search?q=spider&form=basic&start=211',solve_cloudflare=True)
print(response.html_content)
print(response)