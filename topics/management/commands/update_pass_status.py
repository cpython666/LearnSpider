# api/management/commands/update_pass_status.py

from django.core.management.base import BaseCommand
from topics.models import Topics


class Command(BaseCommand):
    help = "批量更新题目的 pass_status 字段为 false"

    def handle(self, *args, **kwargs):
        updated_count = Topics.objects.update(pass_status=False)
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully updated pass_status for {updated_count} topics"
            )
        )
