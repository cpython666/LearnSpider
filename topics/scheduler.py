# myapp/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger  # 使用 CronTrigger
from topics.tasks import fetch_and_save_news  # 假设你有任务在 tasks.py 中


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        fetch_and_save_news,
        trigger=CronTrigger(
            minute="0,10,20,30,40,50"
        ),  # 每个整十分（00, 10, 20, 30, 40, 50）执行一次
        # trigger=IntervalTrigger(minutes=10),  # 每 10 分钟执行一次
        id="fetch_and_save_news",
        name="定时任务:十分钟一次，获取新闻",
        replace_existing=True,
    )
    scheduler.start()
