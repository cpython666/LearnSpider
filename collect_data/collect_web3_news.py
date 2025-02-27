import requests
from topics.models import Web3NewsTag
from pprint import pprint
from urllib.parse import quote
from datetime import datetime
class BianNewsSpider:
    def __init__(self):
        self.headers = {
            'clienttype': 'web',
            'lang': 'zh-cn'
        }
        self.headers_en= {
            'clienttype': 'web',
        }
        self.id_info_mapping=self.merge_tags()

    def fetch_tags(self,en=False):
        json_data = {}
        response = requests.post(
            'https://www.binance.com/bapi/composite/v1/friendly/pgc/news/tags',
            headers=self.headers_en if en else self.headers,
            json=json_data,
        )
        if response.status_code != 200:
            raise Exception('请求失败：', response.status_code, response.text)
        else:
            res = response.json()
            tags = res['data']['data']
            return {_['id']:_ for _ in tags}
    def merge_tags(self):
        tags=list(Web3NewsTag.objects.values_list('tag',flat=True).all())
        id_info_mapping=self.fetch_tags()
        id_info_mapping_en=self.fetch_tags(en=True)
        for tag_id,info in id_info_mapping.items():
            if tag_id in id_info_mapping_en:
                info_en=id_info_mapping_en[tag_id]
                info_en.pop('id')
                info_en.pop('tag')
                info|={f"{k}_en":v for k,v in info_en.items()}
                id_info_mapping[tag_id]=info
            if info.get('tag') in tags:
                continue
            else:
                Web3NewsTag.objects.create(tag_id=info.get("id"),name=info.get("name"),desc=info.get("description"),tag=info.get("tag"),name_en=info.get("name_en"),desc_en=info.get("description_en"),url=f"https://www.binance.com/zh-CN/square/news/{quote(info.get('tag').lower())}")
        return id_info_mapping

    def fetch_new_by_tag(self,last_time=None):
        if not last_time:
            page_num=100
        else:
            page_num=0
        params = {
            'pageIndex': '1',
            'pageSize': '20',
            'tagId': '15',
        }
        response = requests.get(
            'https://www.binance.com/bapi/composite/v4/friendly/pgc/feed/news/list',
            params=params,
            headers=self.headers,
        )
        if response.status_code != 200:
            raise Exception('请求失败', response.status_code, response.text)
        res=response.json()
        data=res['data']['vos']
        pprint(data)

        news_lst=[{"title":_['title'],"subTitle":_['subTitle'],"webLink":_['webLink'],"authorName":_['title'],"published_time":datetime.fromtimestamp(_['date'])} for _ in data]
        pprint(news_lst)
        for news in news_lst:
            if news['published_time']<=last_time:
                break

        # pprint(response.json())




# if __name__ == '__main__':
#     spider = BianNewsSpider()
#     print(spider.tags)