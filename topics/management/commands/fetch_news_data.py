from django.core.management.base import BaseCommand
from topics.tasks import fetch_and_save_news


# python manage.py fetch_news_data
class Command(BaseCommand):
    help = "批量更新题目的 category，规范化 category"

    def handle(self, *args, **kwargs):
        fetch_and_save_news()
