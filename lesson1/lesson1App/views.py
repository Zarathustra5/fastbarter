from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News

def index(request):
    news = News.objects.all()
    return render(request, 'lesson1App/index.html', {'news': news})

def detail_news(request, news_id):
    detail_news = News.objects.get(pk=news_id)
    return render(request, 'lesson1App/detail-news.html', {'detail_news': detail_news})

def catalog(request):
    # return HttpResponse('<h4>About</h4>')
    return render(request, 'lesson1App/catalog.html')

def help(request):
    return render(request, 'lesson1App/help.html')
