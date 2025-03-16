import requests
from pprint import pprint

params = {
    'is_import': '0',
    'page': '1',
    'type': '0',
}

response = requests.get('https://appapi.blockbeats.cn/v6/flash/list', params=params)
res = response.json()
if res["status"] == 0:
    data = res["data"]
    total = data["total"]
    total_page = data["totalPage"]
    data_lst = data["data"]
    for data_item in data_lst:
        id = data_item["id"]
        url = data_item["h5"]
        title = data_item["title"]
        content = data_item["content"]
        time = data_item["time"]
        add_time = data_item["add_time"]
        rich_text = data_item["rich_text"]

pprint(res)
print(res.keys())
