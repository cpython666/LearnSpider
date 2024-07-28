from django.urls import path
from . import views
from django.urls import path
from .views import topic_view

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('tools', views.tools, name='tools'),
    path('shorthand', views.shorthand, name='shorthand'),
    path('solutions', views.solutions, name='solutions'),



    # topic开头重定向到视图返回/html
    path('page/<str:response_path>/', topic_view, name='topic_view'),



    # 请求视图类型
    path('view/hello-spider/', views.hello_spider, name='request_twice'),
    path('view/request-twice/', views.request_twice, name='request-twice'),
    path('view/ua/', views.ua, name='ua'),
    path('view/encode/', views.encode_page, name='encode'),



    # 混合请求接口类型
    path('demo/', views.demo),
    path('demo1/', views.demo1),

]

