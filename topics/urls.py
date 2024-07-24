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

    # 直接请求接口类型
    path('demo/', views.demo),
    path('view/request-twice/', views.request_twice, name='request-twice'),

    # topic开头重定向到视图返回/html
    path('topic/<str:response_path>/', topic_view, name='topic_view'),



]

