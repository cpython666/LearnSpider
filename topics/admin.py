from django.contrib import admin
from .models import Topics

class TopicsAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_id', 'category', 'difficulty', 'pass_status')
    list_editable = ('order_id',)  # 允许在列表中编辑 order_id

admin.site.register(Topics, TopicsAdmin)