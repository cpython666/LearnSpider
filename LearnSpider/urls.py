from django.contrib import admin
from django.urls import include,path,re_path
from django.views.static import serve
from LearnSpider.settings import STATIC_ROOT
# https://www.cnblogs.com/ddb1-1/p/12455147.html
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('topics.urls')),
    path('', include('api.urls')),
]
# re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),#static文件
# 在项目根目录的 urls.py 中定义全局404处理
from topics.views import error404
from django.conf.urls import handler404
handler404 = error404