# Generated by Django 5.0.7 on 2024-07-20 09:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0007_alter_topics_des_alter_topics_goal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topics',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='solution_txt',
            field=models.URLField(blank=True, default='暂无表述', help_text='题解，图文讲解', null=True),
        ),
    ]