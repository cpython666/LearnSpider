from django.urls import path
from . import views
from django.urls import path
from .views import topic_view


urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('topic/<str:response_path>/', topic_view, name='topic_view'),
    # path('topic/<response_path:str>/', topic_view, name='topic_view'),

]