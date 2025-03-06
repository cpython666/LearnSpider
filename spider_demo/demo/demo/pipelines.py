# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewsPipeline:
    def process_item(self, item, spider):
        # 数据清洗或验证的逻辑
        item["title"] = item["title"].strip()  # 去除标题前后的空格
        print(f"pipeline item: {item}")
        return item
