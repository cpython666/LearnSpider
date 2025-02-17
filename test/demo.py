import requests

# res=requests.get('https://www.whu.edu.cn/')
res = requests.get("http://localhost:8001/view/encode/")
# res=requests.get('http://localhost:8001/demo1/')
print(res.text)
print(res.encoding)
