import requests
res=requests.get('http://localhost:8001/request_twice/')
print(res.text)
print(res.encoding)
