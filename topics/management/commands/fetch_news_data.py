from django.core.management.base import BaseCommand
from collect_data.collect_news import get_all_platforms,fetch_platform_news
from topics.models import News,NewsCategory,NewsPlatform,NewsRequestHistory
# python manage.py fetch_news_data
class Command(BaseCommand):
    help = '批量更新题目的 category，规范化 category'

    def handle(self, *args, **kwargs):
        for platform in  get_all_platforms():
            data=fetch_platform_news(platform)
            if data:

                ...