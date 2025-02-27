from django.core.management.base import BaseCommand
from topics.tasks import fetch_and_save_news


# python manage.py fetch_news_data
class Command(BaseCommand):
    help = "采集一批热点新闻"

    def handle(self, *args, **kwargs):
        fetch_and_save_news()
