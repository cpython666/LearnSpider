from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Topics


topics_path_prefix='topics/list/'
topics_path_suffix='.html'

def index(request):
    return render(request, 'topics/index.html')

def list(request):
    return render(request, 'topics/list.html')

def topic_view(request, response_path):
    # 根据 path 获取对应的题目
    topic = get_object_or_404(Topics, response_path=response_path)
    # 返回对应的 HTML 视图
    return render(request, topics_path_prefix+response_path+topics_path_suffix, {'topic': topic})
