from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Topics

from LearnSpider.settings import topics_path_prefix


def index(request):
    return render(request, 'topics/index.html')

def list(request):
    return render(request, 'topics/list.html')
def tools(request):
    return render(request, 'topics/tools.html')
def shorthand(request):
    return render(request, 'topics/shorthand.html')
def solutions(request):
    return render(request, 'topics/solutions.html')

def topic_view(request, response_path):
    # 根据 path 获取对应的题目
    topic = get_object_or_404(Topics, response_path=response_path)
    # 返回对应的 HTML 视图
    return render(request, 'topics/list/'+response_path+'.html', {'topic': topic})

def error404(request, exception):
    return render(request, 'topics/404.html', status=404)
