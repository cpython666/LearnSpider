from django.core.management.base import BaseCommand
from collect_data.collect_news_binance import BianNewsSpider


# python manage.py fetch_news_web3
class Command(BaseCommand):
    help = "批量更新题目的 category，规范化 category"

    def handle(self, *args, **kwargs):
        spider = BianNewsSpider()
        print(spider.id_info_mapping)
        # spider.fetch_new_by_tag()
