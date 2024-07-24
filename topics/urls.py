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
    path('topic/<str:response_path>/', topic_view, name='topic_view'),
    path('demo/', views.demo),
    path('request_twice/', views.request_twice),
]

