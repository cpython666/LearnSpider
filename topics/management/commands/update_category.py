from django.core.management.base import BaseCommand
from topics.models import Topics


# python manage.py update_category
class Command(BaseCommand):
    help = '批量更新题目的 category，规范化 category'

    def handle(self, *args, **kwargs):
        questions = Topics.objects.all()
        for question in questions:
            if question.category:
                question.category = '，'.join(
                    question.category.replace(',', '，').replace('；', '，').replace(';', '，').split('，'))
                question.save()
        self.stdout.write(self.style.SUCCESS('已成功规范化 category 字段'))
