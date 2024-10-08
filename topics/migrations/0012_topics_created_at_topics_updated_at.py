# Generated by Django 5.0.7 on 2024-07-20 18:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0011_remove_topics_created_at_remove_topics_updated_at'),
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
    ]
