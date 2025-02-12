from django.core.management.base import BaseCommand
from topics.models import Topics


# python manage.py update_order_ids
class Command(BaseCommand):
    help = '批量更新题目的 order_id，根绝题目的 order_id 排序好乘以 10'

    def handle(self, *args, **kwargs):
        questions = Topics.objects.all().order_by('order_id')
        for idx, question in enumerate(questions):
            question.order_id = (idx + 1) * 10
            question.save()
        self.stdout.write(self.style.SUCCESS('已成功更新 order_ids'))
