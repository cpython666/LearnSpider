from DrissionPage import Chromium

chrome = Chromium()
new_tab=chrome.new_tab()
new_tab.get("https://www.baidu.com/")
print(new_tab.ele('x://title').text)