from django.core.management.base import BaseCommand
from topics.models import Topics

class Command(BaseCommand):
    help = '批量更新题目的 difficulty_score 字段，规则为目前的 difficulty_score 排序号乘以 10'

    def handle(self, *args, **kwargs):
        questions = Topics.objects.all().order_by('difficulty_score')
        for idx, question in enumerate(questions):
            question.difficulty_score = (idx + 1) * 10
            question.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated difficulty_scores'))
