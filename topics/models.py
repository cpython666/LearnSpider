from django.db import models
import json


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True
    )  # 创建时间
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)  # 修改时间

    class Meta:
        abstract = True


class OrderMixin(models.Model):
    display_order = models.PositiveIntegerField(
        blank=True, null=True, default=100
    )  # 记录显示顺序

    class Meta:
        abstract = True


class Category(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=200, help_text="类别名")
    detail = models.CharField(
        blank=True, null=True, default=None, max_length=200, help_text="类别的描述"
    )

    class Meta:
        db_table = "sd_ls_category"  # 自定义表名


class Topics(BaseModel):
    DIFFICULTY_CHOICES = [
        ("beginner", "初级"),
        ("intermediate", "中级"),
        ("advanced", "高级"),
        ("ultimate", "终极"),
    ]

    id = models.AutoField(primary_key=True)
    order_id = models.PositiveIntegerField(
        blank=True, null=True, default=3, help_text="题目排序，根据难度分排序，会变"
    )
    title = models.CharField(
        blank=True,
        default=None,
        max_length=200,
        help_text="题目的标题，最好有趣个性化一点",
    )
    detail = models.TextField(
        blank=True,
        null=True,
        default="暂无表述",
        help_text="题目的描述：简单创造一个背景故事",
    )
    goal = models.TextField(
        blank=True, null=True, default="暂无描述", help_text="题目的目标：掌握xxx"
    )
    question = models.TextField(
        blank=True, null=True, default="暂无题目要求", help_text="题目要求"
    )
    answer = models.CharField(
        blank=True, null=True, max_length=255, help_text="题目的答案"
    )
    category = models.CharField(
        blank=True,
        null=True,
        default="成神之路",
        max_length=100,
        help_text="题目类别：成神之路，xpath特训",
    )
    difficulty = models.CharField(
        blank=True,
        null=True,
        default="简单",
        max_length=12,
        choices=DIFFICULTY_CHOICES,
        help_text="难度",
    )
    difficulty_score = models.BigIntegerField(
        blank=True,
        null=True,
        default=200,
        help_text="难度分数，后续根据此字段排序order_id",
    )
    points = models.TextField(
        blank=True,
        null=True,
        default="暂未更新考点",
        help_text="本题的考点",
    )
    published = models.BooleanField(
        blank=True, null=True, default=False, help_text="是否发布"
    )
    pass_status = models.BooleanField(
        blank=True, null=True, default=False, help_text="是否通过"
    )
    solution_txt = models.URLField(
        blank=True, null=True, default="暂无表述", help_text="题解，图文讲解"
    )
    solution_video = models.URLField(
        blank=True, null=True, default="暂无表述", help_text="视频讲解"
    )
    api_type = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        default="直接对应视图",
        help_text="此题目的接口类型：直接对应视图，访问一个接口判断后决定是否返回视图，返回一个视图+【多个】api",
    )
    api_prefix = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        default="topic/",
        help_text="topic/,view/,api/",
    )
    response_path = models.TextField(
        blank=True, null=True, help_text="题目路径【文件名】"
    )

    class Meta:
        db_table = "sd_ls_topic"  # 自定义表名
        ordering = ["order_id"]  # 默认按 order_id 排序

    def __str__(self):
        return self.title


# 题目与 Category 的中间表
class TopicCategoryRelation(BaseModel, OrderMixin):
    id = models.AutoField(primary_key=True)

    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "sd_ls_topic_category_relation"  # 自定义表名
        unique_together = ("topic", "category")  # 确保唯一关系

    def __str__(self):
        return f"Topic {self.topic_id} - Category {self.category_id}"


# 平台表
class NewsPlatform(BaseModel):
    name = models.CharField(max_length=100)  # 平台名称
    slug = models.SlugField(unique=True)  # 用于URL的标识符
    description = models.CharField(blank=True, null=True, max_length=255)  # 平台简介

    class Meta:
        db_table = "sd_ls_news_platform"

    def __str__(self):
        return self.name


# 新闻类别表
class NewsCategory(BaseModel):
    name = models.CharField(max_length=100)  # 类别名称
    slug = models.CharField(unique=True, max_length=255)  # 用于URL的标识符
    description = models.TextField(blank=True, null=True)  # 类别简介

    class Meta:
        db_table = "sd_ls_news_category"

    def __str__(self):
        return self.name


class NewsRequestHistory(BaseModel):
    request_time = models.DateTimeField(auto_now_add=True)
    response_data = models.JSONField()  # 处理后的结果数据
    status = models.CharField(blank=True, null=True, max_length=255)
    platform = models.ForeignKey(
        NewsPlatform, related_name="history", on_delete=models.CASCADE
    )  # 所属平台

    class Meta:
        db_table = "sd_ls_news_request_history"

    def __str__(self):
        return f"Request at {self.request_time}"


# 新闻表
class News(BaseModel):
    title = models.CharField(max_length=200)  # 新闻标题
    url = models.CharField(
        blank=True, null=True, unique=True, max_length=255
    )  # 新闻链接
    desc = models.CharField(max_length=500, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    timestamp = models.BigIntegerField(default=0, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()  # 新闻内容
    hot = models.IntegerField(default=0)  # 新闻内容
    platform = models.ForeignKey(
        NewsPlatform,
        related_name="news",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )  # 所属平台
    category = models.ForeignKey(
        NewsCategory,
        related_name="news",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )  # 新闻类别

    class Meta:
        db_table = "sd_ls_news"

    def __str__(self):
        return self.title
