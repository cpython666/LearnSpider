from DrissionPage import ChromiumPage
page = ChromiumPage()
page.get('http://localhost:8001/view/request-twice/')
print(page.html)
page.quit()