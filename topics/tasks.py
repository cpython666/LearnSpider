# myapp/tasks.py
from collect_data.collect_news import get_all_platforms, fetch_platform_news
from topics.models import News, NewsPlatform, NewsRequestHistory
from time import sleep


def fetch_and_save_news():
    for platform_slug in get_all_platforms():
        platform = NewsPlatform.objects.get(slug=platform_slug)
        print(f"采集{platform.name} {platform.slug}中...")
        data = fetch_platform_news(platform.slug)
        if data:
            for item in data:
                try:
                    item = item | {"platform": platform}
                    News.objects.create(**item)
                except Exception as e:
                    continue
            NewsRequestHistory.objects.create(response_data=data, platform=platform)
            # 检查记录数量，如果超过100，则删除前50条
            total=NewsRequestHistory.objects.count()
            print(f'记录数量:{total}')
            if total > 100:
                # 获取最新的 50 条记录的 ID
                preserve_ids = list(NewsRequestHistory.objects.all().order_by("-id")[:50].values_list("id", flat=True))
                # 删除不在这些 ID 中的记录
                NewsRequestHistory.objects.exclude(id__in=preserve_ids).delete()
            print(f"{platform.name} {platform.slug} 保存完成")
        else:
            print(f"请求出错了！")
        sleep(1)
