from django.shortcuts import render

def index(request):
    return render(request, 'topics/index.html')

def list(request):
    return render(request, 'topics/list.html')
