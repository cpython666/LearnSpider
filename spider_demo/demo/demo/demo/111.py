import requests

cookies = {
    'Hm_lvt_6146f11e5afab71309b3accbfc4a932e': '1764859915',
    'HMACCOUNT': '4195C68403711BDB',
    'JSESSIONID': '20B0AEAF19C45427137527C61B0BF1B9',
    'Hm_lpvt_6146f11e5afab71309b3accbfc4a932e': '1764860618',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Authorization': 'ce+UYBd/57Gm1mfc2GZw8uk8ZYaXBre+H3X07uULa+W3tuVrunrhCtiiA7Affyue6AKPopmYKvUxYMyS6ixZ7/+dU6R8DUvNm+4KSYbklU6n7B4y5mY5YmhoZVX4Jb7SklDsDXE9yh7FV8ZWb7mmhEgGgmVjMq7PXPgzCb00pPg=',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/octet-stream',
    'Origin': 'https://www.spolicy.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.spolicy.com/typePolicy?id=2&name=%E6%94%BF%E7%AD%96%E9%80%9A%E7%9F%A5',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = '\n\x012\x12\x00\x1a\x00"\x00*\x002\x008\x00@\x03H\n'

response = requests.post('https://www.spolicy.com/info_api/policyType/showPolicyType', cookies=cookies, headers=headers, data=data)
print(response.json())
print(response)