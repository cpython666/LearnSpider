from DrissionPage import Chromium,ChromiumOptions
from pprint import pprint
co=ChromiumOptions()
co.set_local_port(9999)
chrome = Chromium(addr_or_opts=co)
new_tab=chrome.new_tab()
new_tab.listen.start("policyinfoSearchController/searchEsPolicyinfo")
new_tab.get("https://www.spolicy.com/search?keyword=%E4%BA%BA%E5%B7%A5%E8%BD%AF%E4%BB%B6&type=0")
# new_tab.ele('x://span[contains(text(),"搜索")]').click()
# new_tab.ele('css:.q-placeholder').input("人工软件")
# new_tab.ele('//button//span[@class="text-base" and contains(text(), "搜索")]').click()
res = new_tab.listen.wait()
data = res.response.body
pprint(data)
