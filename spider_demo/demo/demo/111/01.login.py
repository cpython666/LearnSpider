from DrissionPage import Chromium,ChromiumOptions
co=ChromiumOptions()
co.set_local_port(9999)
chrome = Chromium(addr_or_opts=co)
new_tab=chrome.new_tab()
new_tab.get("https://www.spolicy.com/typePolicy?id=2&name=政策通知")
