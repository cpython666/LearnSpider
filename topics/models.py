from django.db import models
import json
class Topics(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', '初级'),
        ('intermediate', '中级'),
        ('advanced', '高级'),
        ('ultimate', '终极'),
    ]

    id = models.AutoField(primary_key=True)
    order_id = models.PositiveIntegerField(blank=True, null=True,default=3,help_text='题目排序，根据难度分排序，会变')
    title = models.CharField(blank=True,default='111',max_length=200,help_text='题目的标题，最好有趣个性化一点')
    des = models.TextField(blank=True, null=True,default='暂无表述',help_text='题目的描述：简单创造一个背景故事')
    goal = models.TextField(blank=True, null=True,default='暂无描述',help_text='题目的目标：掌握xxx')
    question = models.TextField(blank=True, null=True,default='暂无题目要求',help_text='题目要求')
    category = models.CharField(blank=True, null=True,default='成神之路',max_length=100,help_text='题目类别：成神之路，xpath特训')
    difficulty = models.CharField(blank=True, null=True,default='简单',max_length=12, choices=DIFFICULTY_CHOICES,help_text='难度')
    difficulty_score = models.BigIntegerField(blank=True, null=True,default=200,help_text='难度分数，后续根据此字段排序order_id')
    points = models.TextField(blank=True, null=True,default='暂未更新考点',help_text='本题的考点',)
    pass_status = models.BooleanField(blank=True, null=True,default=False,help_text='是否通过')
    solution_txt = models.URLField(blank=True, null=True,default='暂无表述',help_text='题解，图文讲解')
    solution_video = models.URLField(blank=True, null=True,default='暂无表述',help_text='视频讲解')
    api_type = models.CharField(blank=True, null=True,max_length=255,default='直接对应视图',help_text='此题目的接口类型：直接对应视图，访问一个接口判断后决定是否返回视图，返回一个视图+【多个】api')
    response_path = models.TextField(blank=True, null=True, help_text='题目路径【文件名】')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['order_id']  # 默认按 order_id 排序

    def __str__(self):
        return self.title