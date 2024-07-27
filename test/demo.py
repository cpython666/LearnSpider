import requests
res=requests.get('http://localhost:8001/view/request-twice/')
print(res.text)
print(res.encoding)