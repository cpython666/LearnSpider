import requests
from pprint import pprint
from topics.models import Topics, News, NewsCategory, NewsPlatform


def fetch_platform_news(platform_slug):
    # 来源：https://hot.hlds.fun/#/
    url = f"https://dailyhotapi.hlds.fun/{platform_slug}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        res = response.json()
        data = res["data"]
        # pprint(data)
        res = []
        for _ in data:
            if type(_["timestamp"]) != "int":
                _["timestamp"] = None
            res.append(
                {
                    "title": _["title"],
                    "url": _["url"],
                    "timestamp": _["timestamp"],
                    "hot": _.get("hot"),
                    "desc": _.get("desc"),
                }
            )
        return res
    else:
        print(response, response.text)


def get_all_platforms():
    platforms = NewsPlatform.objects.values_list("slug", flat=True).all()
    return list(platforms)


if __name__ == "__main__":
    get_all_platforms()
