from django.shortcuts import render
from .models import article


def news(request):
    articles = article.objects.all().order_by('-date_a')
    return render(request, "news.html", {'articels': articles})


# Create your views here.
def news_prev(request, pk):
    news = article.objects.filter(id=pk)
    read = article.objects.exclude(id=pk)[:5]
    return render(request, "detail_news.html", {'data': news, 'read':read})
