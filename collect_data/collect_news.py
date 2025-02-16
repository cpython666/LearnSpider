import requests
from pprint import pprint
from topics.models import Topics, News, NewsCategory, NewsPlatform


def fetch_platform_news(platform_slug):
    # 来源：https://hot.hlds.fun/#/
    response = requests.get(f'https://dailyhotapi.hlds.fun/{platform_slug}')
    if response.status_code == 200:
        res = response.json()
        data = res['data']
        # pprint(data)
        data = [
            {"title": _['title'], "url": _['url'], "timestamp": _['timestamp'], "hot": _['hot'], "desc": _['desc']} for
            _ in
            data
        ]
        return data
    else:
        print(response, response.text)


def get_all_platforms():
    platforms = NewsPlatform.objects.values_list('slug', flat=True).all()
    return list(platforms)


if __name__ == '__main__':
    get_all_platforms()
