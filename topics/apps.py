from django.apps import AppConfig


class TopicsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "topics"

    def ready(self):
        from topics.scheduler import start_scheduler
        from LearnSpider.settings import DJANGO_ENV

        if DJANGO_ENV != "local":
            start_scheduler()
