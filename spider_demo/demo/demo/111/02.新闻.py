from DrissionPage import Chromium,ChromiumOptions
co=ChromiumOptions()
co.set_local_port(9999)
chrome = Chromium(addr_or_opts=co)
new_tab=chrome.new_tab()
new_tab.listen.start("policyType/showPolicyType")
new_tab.get("https://www.spolicy.com/typePolicy?id=2&name=政策通知")
res=new_tab.listen.wait()
data=res.response.body
print("第一页数据:",data)
new_tab.ele('x://span[contains(text(),"加载更多")]').click()
res = new_tab.listen.wait()
data = res.response.body
print(f"第1页数据:", data)
for i in range(2,11):
    new_tab.ele("css:.q-field__control-container input").clear().input(f"{str(i)}\n")
    # new_tab.ele('x://span[contains(text(),"加载更多")]').click()
    res=new_tab.listen.wait()
    data=res.response.body
    print(f"第{i}页数据:",data)
