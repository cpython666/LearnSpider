# 在 api 应用中创建一个 management/commands 文件夹，并在其中创建 update_order_ids.py

from django.core.management.base import BaseCommand
from topics.models import Topics

class Command(BaseCommand):
    help = '批量更新题目的 order_id，根绝题目的难度分数排序order_id'

    def handle(self, *args, **kwargs):
        questions = Topics.objects.all().order_by('difficulty_score')
        for idx, question in enumerate(questions):
            question.order_id = idx + 1
            question.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated order_ids'))
